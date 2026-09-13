import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_footer(num_pages)
            super().showPage()
        super().save()

    def draw_footer(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        # Header rule & title
        self.drawString(54, 750, "AI Academic & Career Navigator | Official Portfolio Summary")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 742, 558, 742)
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 40, page_str)
        self.drawString(54, 40, "Confidential - Prepared for Student Academic & Career Planning")
        self.line(54, 52, 558, 52)
        self.restoreState()

def generate_progress_report_pdf(student_data: dict) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=64,
        bottomMargin=64
    )

    styles = getSampleStyleSheet()
    primary_color = colors.HexColor("#1E3A8A")
    text_dark = colors.HexColor("#0F172A")
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        spaceAfter=4
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=primary_color,
        spaceBefore=12,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=text_dark
    )
    bold_body = ParagraphStyle(
        'BoldBody',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("Career Readiness & Progress Audit Report", title_style))
    date_str = datetime.now().strftime("%B %d, %Y")
    story.append(Paragraph(f"Generated on: {date_str} | Academic Milestone Assessment", body_style))
    story.append(Spacer(1, 10))

    # Student Profile Banner Table
    p = student_data.get("profile", {}) or {}
    profile_data = [
        [Paragraph(f"<b>Student Name:</b> {p.get('name', 'N/A')}", body_style),
         Paragraph(f"<b>Academic Field:</b> {p.get('field', 'N/A')}", body_style)],
        [Paragraph(f"<b>University:</b> {p.get('university', 'N/A')}", body_style),
         Paragraph(f"<b>Degree/Level:</b> {p.get('degree', 'N/A')} ({p.get('current_year', 'Year 1')})", body_style)],
        [Paragraph(f"<b>Preferred Career:</b> {p.get('preferred_career', 'N/A')}", body_style),
         Paragraph(f"<b>Current Semester:</b> {p.get('current_semester', 'N/A')}", body_style)]
    ]
    t_profile = Table(profile_data, colWidths=[250, 254])
    t_profile.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F8FAFC")),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#E2E8F0")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(t_profile)
    story.append(Spacer(1, 10))

    # Career Readiness Score Summary
    history = student_data.get("assessment_history", []) or []
    baseline = student_data.get("baseline_assessment") or {}
    current_assessment = (history[-1] if history else baseline) or {}
    prev_assessment = (history[-2] if len(history) >= 2 else current_assessment) or {}

    curr_score = current_assessment.get("overall_score", 0)
    prev_score = prev_assessment.get("overall_score", 0)
    diff = curr_score - prev_score
    diff_symbol = f"+{diff}" if diff > 0 else f"{diff}"

    story.append(Paragraph("1. Career Readiness Index", h1_style))
    score_table_data = [
        [Paragraph("<b>Current Index</b>", bold_body), Paragraph("<b>Previous Index</b>", bold_body), Paragraph("<b>Net Growth</b>", bold_body)],
        [Paragraph(f"<font size=14 color='#1E3A8A'><b>{curr_score} / 100</b></font>", body_style),
         Paragraph(f"<font size=14 color='#475569'><b>{prev_score} / 100</b></font>", body_style),
         Paragraph(f"<font size=14 color='#059669'><b>{diff_symbol} pts</b></font>", body_style)]
    ]
    t_score = Table(score_table_data, colWidths=[168, 168, 168])
    t_score.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#BFDBFE")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(t_score)
    story.append(Spacer(1, 10))

    # Category Breakdown Matrix
    story.append(Paragraph("2. Category Performance Comparison", h1_style))
    curr_cats = current_assessment.get("category_scores", {}) or {}
    prev_cats = prev_assessment.get("category_scores", {}) or {}

    cat_rows = [
        [Paragraph("<b>Evaluation Category</b>", bold_body),
         Paragraph("<b>Previous</b>", bold_body),
         Paragraph("<b>Current</b>", bold_body),
         Paragraph("<b>Variance</b>", bold_body)]
    ]
    categories = ["academic", "skills", "projects", "experience", "certifications", "activities", "networking", "portfolio"]
    for c in categories:
        c_curr = float(curr_cats.get(c, 0))
        c_prev = float(prev_cats.get(c, 0))
        c_diff = round(c_curr - c_prev, 1)
        d_str = f"+{c_diff}%" if c_diff > 0 else f"{c_diff}%"
        cat_rows.append([
            Paragraph(c.capitalize(), body_style),
            Paragraph(f"{c_prev}%", body_style),
            Paragraph(f"{c_curr}%", body_style),
            Paragraph(f"<b>{d_str}</b>", body_style)
        ])

    t_cat = Table(cat_rows, colWidths=[180, 108, 108, 108])
    t_cat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(t_cat)
    story.append(Spacer(1, 10))

    # Academic & Skills Summary
    story.append(Paragraph("3. Academic Standing & Skill Trajectory", h1_style))
    skills = student_data.get("skills", []) or []
    skill_text = ", ".join([f"{s.get('name', 'Skill')} ({s.get('level', 'Beginner')})" for s in skills]) if skills else "No skills listed."
    story.append(Paragraph(f"<b>Current Active Skill Stack:</b> {skill_text}", body_style))
    story.append(Spacer(1, 6))

    # Achievements & Milestones
    story.append(Paragraph("4. Verified Achievements & Honors", h1_style))
    achs = student_data.get("achievements", []) or []
    if achs:
        for a in achs:
            title = a.get('title', 'Honor')
            org = a.get('organization', 'Institution')
            dt = a.get('date', '')
            desc = a.get('description', '')
            story.append(Paragraph(f"• <b>{title}</b> — {org} ({dt})<br/>&nbsp;&nbsp;{desc}", body_style))
            story.append(Spacer(1, 3))
    else:
        story.append(Paragraph("No verified achievements recorded yet.", body_style))
    story.append(Spacer(1, 8))

    # AI Progress Audit & Recommendations
    story.append(Paragraph("5. AI Progress Evaluation & Immediate Strategic Next Steps", h1_style))
    analysis_text = current_assessment.get("ai_analysis", "Baseline established. Initial career and skill targets mapped.")
    story.append(Paragraph(analysis_text, body_style))
    story.append(Spacer(1, 6))

    recs = current_assessment.get("ai_recommendations", []) or []
    if recs:
        story.append(Paragraph("<b>Prioritized Action Items:</b>", bold_body))
        for r in recs:
            story.append(Paragraph(f"→ {r}", body_style))
            story.append(Spacer(1, 2))

    doc.build(story, canvasmaker=NumberedCanvas)
    buffer.seek(0)
    return buffer.getvalue()

def generate_career_portfolio_pdf(student_data: dict) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=64,
        bottomMargin=64
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'PortfolioTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A")
    )
    h1_style = ParagraphStyle(
        'PortfolioH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#0284C7"),
        spaceBefore=12,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'PortfolioBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1E293B")
    )

    story = []
    p = student_data.get("profile", {}) or {}
    story.append(Paragraph(f"{p.get('name', 'Student Name')} — Career Portfolio", title_style))
    story.append(Paragraph(f"{p.get('degree', 'Degree')} | {p.get('university', 'University')} | Target: {p.get('preferred_career', 'Career')}", body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Executive Career Objective", h1_style))
    story.append(Paragraph(p.get("career_goals") or "No stated career objective provided.", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Technical & Professional Skills", h1_style))
    skills = student_data.get("skills", []) or []
    if skills:
        s_table_data = [[Paragraph("<b>Skill</b>", body_style), Paragraph("<b>Proficiency</b>", body_style), Paragraph("<b>Target</b>", body_style)]]
        for sk in skills:
            s_table_data.append([
                Paragraph(sk.get("name", "N/A"), body_style),
                Paragraph(sk.get("level", "N/A"), body_style),
                Paragraph(sk.get("target_level", "N/A"), body_style)
            ])
        t_sk = Table(s_table_data, colWidths=[200, 150, 154])
        t_sk.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F0F9FF")),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#BAE6FD")),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        story.append(t_sk)
    else:
        story.append(Paragraph("No technical or professional skills recorded yet.", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Featured Projects", h1_style))
    projects = student_data.get("projects", []) or []
    if projects:
        for proj in projects:
            story.append(Paragraph(f"• <b>{proj.get('title', 'Project')}</b> [{proj.get('status', 'In Progress')}]", body_style))
            story.append(Paragraph(f"  {proj.get('description', '')}", body_style))
            tech_stack = ", ".join(proj.get('technologies', [])) if proj.get('technologies') else "General Tools"
            story.append(Paragraph(f"  <i>Tech Stack:</i> {tech_stack} | URL: {proj.get('github_url', 'N/A')}", body_style))
            story.append(Spacer(1, 4))
    else:
        story.append(Paragraph("No practical projects recorded yet.", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Verified Achievements & Honors", h1_style))
    achs = student_data.get("achievements", []) or []
    if achs:
        for ach in achs:
            story.append(Paragraph(f"🏆 <b>{ach.get('title', 'Honor')}</b> ({ach.get('date', '')}) — {ach.get('organization', '')}", body_style))
            story.append(Paragraph(f"   {ach.get('description', '')}", body_style))
            story.append(Spacer(1, 4))
    else:
        story.append(Paragraph("No verified achievements recorded yet.", body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    buffer.seek(0)
    return buffer.getvalue()