import os
import io
import fitz  # PyMuPDF
import chromadb
from typing import List, Dict, Any
from src.utils import call_gemini

CHROMA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "chroma_storage")

def get_chroma_client():
    os.makedirs(CHROMA_DIR, exist_ok=True)
    return chromadb.PersistentClient(path=CHROMA_DIR)

def extract_pdf_text(file_bytes: bytes) -> str:
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text_pages = []
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")
            if text.strip():
                text_pages.append(text)
        return "\n\n".join(text_pages)
    except Exception as exc:
        return f"ERROR: Failed extracting text from PDF: {str(exc)}"

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 150) -> List[str]:
    if not text:
        return []
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def index_course_catalog(catalog_pdf_bytes: bytes, collection_name: str = "course_catalog") -> int:
    raw_text = extract_pdf_text(catalog_pdf_bytes)
    if not raw_text or raw_text.startswith("ERROR:"):
        return 0
    
    chunks = chunk_text(raw_text)
    if not chunks:
        return 0
    
    client = get_chroma_client()
    try:
        client.delete_collection(name=collection_name)
    except Exception:
        pass
    
    collection = client.create_collection(name=collection_name)
    ids = [f"chk_{i}" for i in range(len(chunks))]
    metadatas = [{"source": "uploaded_catalog", "chunk_id": i} for i in range(len(chunks))]
    
    collection.add(
        documents=chunks,
        metadatas=metadatas,
        ids=ids
    )
    return len(chunks)

def retrieve_courses(query: str, n_results: int = 4, collection_name: str = "course_catalog") -> List[Dict[str, Any]]:
    client = get_chroma_client()
    try:
        collection = client.get_collection(name=collection_name)
    except Exception:
        return []
    
    count = collection.count()
    if count == 0:
        return []
    
    actual_k = min(n_results, count)
    results = collection.query(query_texts=[query], n_results=actual_k)
    
    docs = []
    if results and "documents" in results and results["documents"]:
        retrieved_texts = results["documents"][0]
        retrieved_metas = results["metadatas"][0] if "metadatas" in results else [{}] * len(retrieved_texts)
        for doc_text, meta in zip(retrieved_texts, retrieved_metas):
            docs.append({"content": doc_text, "metadata": meta})
    return docs

def ask_catalog_rag(question: str, collection_name: str = "course_catalog") -> str:
    contexts = retrieve_courses(question, n_results=3, collection_name=collection_name)
    if not contexts:
        return "No relevant university catalog documents found. Please upload a university handbook or course catalog PDF."
    
    context_str = "\n---\n".join([c["content"] for c in contexts])
    system_prompt = (
        "You are an academic university advisor assistant. Answer the student question STRICTLY using the provided "
        "university catalog context. If the answer is not contained in the context, explicitly declare: "
        "'Based on the uploaded catalog, this information is not available.' NEVER invent courses, codes, or prerequisites."
    )
    user_prompt = f"Context from Handbook:\n{context_str}\n\nStudent Question: {question}"
    return call_gemini(user_prompt, system_instruction=system_prompt)