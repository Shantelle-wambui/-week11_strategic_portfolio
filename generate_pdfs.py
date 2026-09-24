"""
generate_pdfs.py
Generates 4 PDFs for Week 11 submission:
  - CV_ShantelleWambuiKungu_DataAnalyst.pdf
  - Week11_Business_Case_ShantelleWambuiKungu.pdf
  - LinkedIn_Header_About_ShantelleWambuiKungu.pdf
  - Week11_Self_Reflection_ShantelleWambuiKungu.pdf
"""

from fpdf import FPDF
from fpdf.enums import XPos, YPos
import re

OUT = "/home/shantel/week11_strategic_portfolio/"

def clean(text):
    """Replace characters outside latin-1 range with ASCII equivalents."""
    replacements = {
        '\u2014': '-', '\u2013': '-', '\u2022': '*',
        '\u2019': "'", '\u2018': "'", '\u201c': '"', '\u201d': '"',
        '\u2026': '...', '\u00b0': 'deg', '\u00a0': ' ',
        '\u2192': '->', '\u2190': '<-', '\u2713': 'v', '\u2265': '>=',
        '\u2264': '<=', '\u00d7': 'x', '\u00f7': '/',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text

# ── Colour palette ─────────────────────────────────────────────────────────
NAVY   = (15,  23,  42)
ACCENT = (16, 185, 129)   # emerald green
WHITE  = (255, 255, 255)
LGREY  = (148, 163, 184)
DGREY  = (30,  41,  59)
RED    = (239,  68,  68)
GREEN  = (34, 197,  94)
AMBER  = (245, 158,  11)
BLACK  = (15,  23,  42)


# ══════════════════════════════════════════════════════════════════════════════
# BASE CLASS
# ══════════════════════════════════════════════════════════════════════════════
class BasePDF(FPDF):
    def __init__(self, title=""):
        super().__init__()
        self.doc_title = title
        self.set_margins(18, 18, 18)
        self.set_auto_page_break(auto=True, margin=18)

    def header(self):
        pass

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(*LGREY)
        self.cell(0, 5, f"Shantelle Wambui Kungu  |  PLP AI/ML Programme  |  {self.doc_title}",
                  align="C")

    def section_heading(self, text, accent_color=ACCENT):
        self.ln(4)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*accent_color)
        self.cell(0, 7, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # underline bar
        self.set_draw_color(*accent_color)
        self.set_line_width(0.5)
        x = self.get_x()
        y = self.get_y()
        self.line(x, y, x + 174, y)
        self.ln(3)
        self.set_text_color(*BLACK)

    def body(self, text, size=10):
        self.set_font("Helvetica", "", size)
        self.set_text_color(*BLACK)
        self.multi_cell(0, 5.5, clean(text), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def bold_body(self, label, value, size=10):
        self.set_font("Helvetica", "B", size)
        self.set_text_color(*BLACK)
        self.write(5.5, clean(f"{label}: "))
        self.set_font("Helvetica", "", size)
        self.write(5.5, clean(value))
        self.ln(6)

    def bullet(self, text, size=10, indent=4):
        self.set_font("Helvetica", "", size)
        self.set_text_color(*BLACK)
        self.set_x(self.get_x() + indent)
        self.multi_cell(0, 5.5, clean(f"*  {text}"), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def kpi_row(self, items):
        """Render a row of coloured KPI boxes."""
        w = 174 / len(items)
        x_start = self.get_x()
        y = self.get_y()
        colors = [GREEN, ACCENT, AMBER]
        for i, (label, val) in enumerate(items):
            self.set_fill_color(*DGREY)
            self.set_xy(x_start + i * w, y)
            self.rect(x_start + i * w, y, w - 2, 14, "F")
            self.set_xy(x_start + i * w, y + 1)
            self.set_font("Helvetica", "B", 13)
            self.set_text_color(*colors[i % 3])
            self.cell(w - 2, 6, val, align="C",
                      new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            self.set_xy(x_start + i * w, y + 7)
            self.set_font("Helvetica", "", 8)
            self.set_text_color(*LGREY)
            self.cell(w - 2, 5, label, align="C")
        self.ln(18)
        self.set_text_color(*BLACK)

    def divider(self):
        self.ln(2)
        self.set_draw_color(*DGREY)
        self.set_line_width(0.2)
        self.line(self.get_x(), self.get_y(), self.get_x() + 174, self.get_y())
        self.ln(3)


# ══════════════════════════════════════════════════════════════════════════════
# 1. CV
# ══════════════════════════════════════════════════════════════════════════════
def make_cv():
    pdf = BasePDF("CV")
    pdf.add_page()

    # Header block
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 38, "F")
    pdf.set_xy(18, 7)
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 9, "SHANTELLE WAMBUI KUNGU", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(18, 17)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 6, "Data Analyst  |  AI/ML Engineer  |  Operational Intelligence",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(18, 25)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*LGREY)
    pdf.cell(0, 5,
             "Nairobi, Kenya  |  0768 540 301  |  shantellewambuikungu@gmail.com  |  github.com/Shantelle-wambui",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_y(44)
    pdf.set_text_color(*BLACK)

    # Summary
    pdf.section_heading("PROFESSIONAL SUMMARY")
    pdf.body(
        "Data Analyst and AI/ML Engineer with production experience building end-to-end intelligent "
        "systems across fraud detection, predictive maintenance, safety monitoring, and operational "
        "analytics. Co-built ClaimGuard - a production-grade insurance fraud detection platform "
        "achieving AUC-ROC 0.84, cutting claim review time from 5-15 days to under 30 seconds, and "
        "projecting KES 148M in annual savings for a mid-size insurer. Full-stack Software Engineering "
        "Intern at E&M Techhouse (INUKA/PLP), shipping features across six live products."
    )

    # Skills
    pdf.section_heading("TECHNICAL SKILLS")
    skills = [
        ("ML & Data Science", "XGBoost, scikit-learn, SHAP, pandas, NumPy, SMOTE, Plotly, Matplotlib"),
        ("Data Engineering",  "ETL pipeline design, PostgreSQL, SQLAlchemy, Alembic, Great Expectations"),
        ("Languages",         "Python, SQL, TypeScript, JavaScript (ES6+), Dart"),
        ("Frameworks",        "FastAPI, Streamlit, Flask, Spring Boot, React, Next.js 14, Flutter"),
        ("Infrastructure",    "Docker, Docker Compose, Celery, Redis, GitHub Actions, Render, Vercel"),
        ("AI/LLM",            "Groq LLM integration, SHAP explainability, XGBoost model registry"),
    ]
    for label, value in skills:
        pdf.bold_body(label, value, size=9)

    # Experience
    pdf.section_heading("PROFESSIONAL EXPERIENCE")
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, 6, "Software Engineering Intern - E&M Techhouse, Nairobi (INUKA/PLP)  |  2025 - Present",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)

    roles = [
        ("ClaimGuard - AI Insurance Fraud Detection (FastAPI + Next.js)", [
            "Co-built production fraud detection platform: AUC-ROC 0.84, Precision 79%, Recall 81%",
            "Engineered 25 features; network/ring detection found 12 fraud rings (KES 4.2M exposure)",
            "Reduced processing time from 5-15 days to under 30 seconds - 95% efficiency gain",
            "Built FastAPI backend: ingestion, ETL, rules engine, ML scoring, audit trail",
            "Built Next.js frontend: case review, HITL queue, network visualisation, ML admin",
        ]),
        ("Sentinel - HSE Early-Warning Platform (Next.js + Spring Boot)", [
            "Built AI HSE Reporting Agent: Groq LLM integration, 15-section regulatory PDF generator",
            "Built context-aware AI chatbot for Q&A over live HSE event data",
        ]),
        ("Ecosystem Banking Platform - Mobile, Frontend & Backend", [
            "Sole Flutter developer: biometric auth, offline-first sync, follow-up calendar, push notifications",
            "React/Next.js: customer management, dashboard, ecosystem modules with live API integration",
            "Spring Boot: account-opening endpoint, Finacle adapter, scheduled follow-up status job",
        ]),
        ("Inuka Pulse - M&E Intelligence Platform (Expo React Native)", [
            "Built Case Manager mobile app: KPI dashboard, at-risk beneficiary caseload, dropout risk scoring",
        ]),
    ]
    for role_title, bullets in roles:
        pdf.set_font("Helvetica", "BI", 10)
        pdf.set_text_color(*ACCENT)
        pdf.cell(0, 5.5, role_title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(*BLACK)
        for b in bullets:
            pdf.bullet(b, size=9)
        pdf.ln(1)

    # Projects
    pdf.section_heading("INDEPENDENT PROJECTS")
    projects = [
        ("Equipment Failure Risk Monitor (Week 10)",
         "Streamlit + XGBoost dashboard scoring 20-machine fleet. ROC-AUC 0.94, Recall 0.83. "
         "Reduced maintenance prioritisation from 2 hours to 2 minutes."),
        ("Supply Chain Optimisation Dashboard (Week 8)",
         "Multi-source data analysis; optimisation models reduced simulated stockouts by 34%."),
        ("ETL Pipeline - Multi-Source Operational Data (Week 4)",
         "Python ETL pipeline across PostgreSQL, CSV, JSON, HTML with Great Expectations validation."),
    ]
    for title, desc in projects:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*BLACK)
        pdf.cell(0, 5.5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Helvetica", "", 9)
        pdf.multi_cell(0, 5, desc, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(1)

    # Education
    pdf.section_heading("EDUCATION")
    edu = [
        ("Certificate - AI & Machine Learning for Operations", "Power Learn Project (PLP) Academy | 2026"),
        ("Software Engineering Certificate", "Moringa School | 2025"),
        ("Diploma in Information Technology", "KCA University | 2024"),
    ]
    for degree, institution in edu:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*BLACK)
        pdf.write(5.5, degree + "  ")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(*LGREY)
        pdf.write(5.5, institution)
        pdf.ln(6)

    pdf.output(OUT + "CV_ShantelleWambuiKungu_DataAnalyst.pdf")
    print("v CV generated")


# ══════════════════════════════════════════════════════════════════════════════
# 2. BUSINESS CASE
# ══════════════════════════════════════════════════════════════════════════════
def make_business_case():
    pdf = BasePDF("Week 11 Business Case")
    pdf.add_page()

    # Header
    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 42, "F")
    pdf.set_xy(18, 6)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 8, "ClaimGuard: AI-Powered Insurance Fraud Detection",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(18, 16)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 6, "Executive Business Case - For CFO / Board Approval",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(18, 25)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*LGREY)
    pdf.cell(0, 5,
             "Prepared by: Shantelle Wambui Kungu  |  September 2026  |  CONFIDENTIAL",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_y(50)
    pdf.set_text_color(*BLACK)

    # 1. Problem
    pdf.section_heading("1. PROBLEM STATEMENT")
    pdf.body(
        "Kenya's motor insurance sector loses an estimated KES 40-60 billion annually to fraudulent "
        "claims (IRA Kenya, 2024). The current manual review process takes 5-15 days per claim and "
        "catches only 40% of fraud. Each missed fraudulent claim costs an average of KES 150,000. "
        "For a mid-size insurer processing 2,000 claims per month, this is KES 14.4M in undetected "
        "fraud losses every month - a direct hit to the combined ratio and shareholder returns.\n\n"
        "The core failure is structural: human reviewers cannot cross-reference hundreds of claims "
        "simultaneously. A garage filing nine fraudulent claims across different policyholders over "
        "90 days is completely invisible to an adjuster reading one file at a time."
    )

    # 2. Solution
    pdf.section_heading("2. PROPOSED SOLUTION")
    pdf.body("ClaimGuard is a production-ready AI claims intelligence platform with three detection layers:")
    pdf.bullet("Rules Engine: 8 hard motor fraud rules (claim within 14 days of inception, duplicate OB numbers, provider billing spikes, round-sum amounts, missing documents)")
    pdf.bullet("XGBoost ML Scorer: 25 engineered features -> fraud probability 0-1. AUC-ROC 0.84 | Precision 79% | Recall 81%")
    pdf.bullet("Network / Ring Detector: Graph analysis across providers, claimants, and vehicles - identifies organised fraud rings invisible to individual reviewers")
    pdf.ln(2)
    pdf.body("Every decision includes a plain-English SHAP explanation for adjusters and a full audit trail for IRA compliance. Processing time: under 30 seconds per claim.")

    # 3. Financial Impact
    pdf.section_heading("3. FINANCIAL IMPACT")
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 5.5, "Assumptions: 2,000 claims/month | 8% fraud rate = 160 fraudulent claims | Avg value KES 150,000",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    table_data = [
        ("Additional fraud caught",   "(81%-40%) x 160 x KES 150K",  "KES 9.84M",  "KES 118.1M"),
        ("Adjuster time savings",     "95% reduction x 8 staff x KES 120K", "KES 0.91M", "KES 10.9M"),
        ("False positive reduction",  "40% fewer wrongly flagged x KES 5K", "KES 1.60M", "KES 19.2M"),
        ("TOTAL SAVINGS",             "",                              "KES 12.35M", "KES 148.2M"),
    ]
    headers = ["Source", "Calculation", "Monthly", "Annual"]
    col_w = [52, 60, 28, 28]

    # table header
    pdf.set_fill_color(*NAVY)
    pdf.set_text_color(*WHITE)
    pdf.set_font("Helvetica", "B", 9)
    for h, w in zip(headers, col_w):
        pdf.cell(w, 6, h, border=0, fill=True, align="C")
    pdf.ln()

    for i, (source, calc, monthly, annual) in enumerate(table_data):
        is_total = i == 3
        pdf.set_fill_color(*(DGREY if is_total else (240, 248, 255)))
        pdf.set_text_color(*(GREEN if is_total else BLACK))
        pdf.set_font("Helvetica", "B" if is_total else "", 9)
        for text, w in zip([source, calc, monthly, annual], col_w):
            pdf.cell(w, 6, text, border=0, fill=True, align="C" if text != source else "L")
        pdf.ln()

    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*BLACK)
    pdf.cell(0, 5.5, "Investment: KES 11.5M (Year 1) - Development KES 8.5M | Cloud KES 1.8M | Maintenance KES 1.2M",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)

    pdf.kpi_row([
        ("Year 1 ROI",     "1,188%"),
        ("Payback Period", "28 Days"),
        ("5-Year NPV",     "KES 580M"),
    ])

    # 4. Risks
    pdf.section_heading("4. RISKS & MITIGATION")
    risks = [
        ("Regulatory challenge - IRA questions automated rejections",
         "Every rejection includes a full SHAP audit trail. Human review is mandatory for all rejections. Designed to comply with IRA data governance guidelines."),
        ("Model drift - fraud patterns evolve faster than the model retrains",
         "Automated monthly retraining with champion/challenger model registry. Alert fires if AUC-ROC drops below 0.78."),
    ]
    for risk, mitigation in risks:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*RED)
        pdf.cell(0, 5.5, f"Risk: {risk}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(*BLACK)
        pdf.multi_cell(0, 5.5, f"Mitigation: {mitigation}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(2)

    # 5. Recommendation
    pdf.section_heading("5. RECOMMENDATION - GO v", accent_color=GREEN)
    pdf.set_fill_color(*DGREY)
    pdf.rect(18, pdf.get_y(), 174, 28, "F")
    pdf.set_xy(22, pdf.get_y() + 3)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*GREEN)
    pdf.cell(0, 6, "Approve full deployment of ClaimGuard.", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(22, pdf.get_y())
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*WHITE)
    pdf.multi_cell(166, 5.5,
        "KES 11.5M investment. KES 148.2M Year 1 return. 28-day payback. "
        "The technology is production-ready.\n"
        "Approvals required: (1) Budget KES 11.5M  (2) IT window Q4 2026  (3) IRA compliance sign-off",
        new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.output(OUT + "Week11_Business_Case_ShantelleWambuiKungu.pdf")
    print("v Business Case generated")


# ══════════════════════════════════════════════════════════════════════════════
# 3. LINKEDIN HEADER + ABOUT
# ══════════════════════════════════════════════════════════════════════════════
def make_linkedin():
    pdf = BasePDF("LinkedIn Profile")
    pdf.add_page()

    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 35, "F")
    pdf.set_xy(18, 8)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 8, "LinkedIn Profile - Header & About Section",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(18, 18)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*LGREY)
    pdf.cell(0, 5, "Shantelle Wambui Kungu  |  Week 11 Submission",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_y(42)

    pdf.section_heading("LINKEDIN HEADLINE")
    pdf.set_fill_color(*DGREY)
    pdf.rect(18, pdf.get_y(), 174, 14, "F")
    pdf.set_xy(22, pdf.get_y() + 3)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 7,
             "Data Analyst & AI/ML Engineer | Insurance Fraud Detection | Full-Stack | Flutter . FastAPI . XGBoost | PLP INUKA",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(8)
    pdf.set_text_color(*BLACK)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "Formula: [What you do] | [Specialisation] | [Key tools] | [Programme signal]",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(4)

    pdf.section_heading("ABOUT SECTION")
    about_paragraphs = [
        "I build systems that turn messy operational data into decisions that protect money, time, and people.",

        "Most recently: co-built ClaimGuard - an AI-powered insurance fraud detection platform for the "
        "Kenyan motor insurance market. It processes claims in under 30 seconds (down from 5-15 days), "
        "catches 81% of fraud, and projects KES 148 million in annual savings for a mid-size insurer. "
        "The system is production-ready: FastAPI backend, XGBoost + SHAP explainability, network/ring "
        "detection, HITL review queue, and a full Next.js frontend.",

        "Before that I was the sole Flutter mobile developer on a live banking platform - shipping "
        "biometric auth, offline-first sync, a follow-up calendar, and push notifications to production. "
        "And built an AI HSE safety platform with a Groq LLM reporting agent that generates 15-section "
        "regulatory-grade PDF reports.",

        "What I work with:\n"
        "  -> Machine learning: XGBoost, scikit-learn, SHAP, SMOTE, pandas, NumPy\n"
        "  -> Backend: FastAPI, Flask, Spring Boot, PostgreSQL, Celery, Docker\n"
        "  -> Frontend/Mobile: React, Next.js 14, Flutter, TypeScript, Tailwind\n"
        "  -> Operational analytics: ETL pipelines, Streamlit dashboards, Plotly",

        "What I care about:\n"
        "Fraud that gets caught before it costs. Equipment that gets fixed before it fails. "
        "Data that tells you the truth fast enough to act on it.",

        "Currently a Software Engineering Intern at E&M Techhouse under the PLP INUKA Programme, "
        "shipping across six live products. Open to data analyst, ML engineer, and operational "
        "intelligence roles.\n\n"
        "Nairobi, Kenya  |  github.com/Shantelle-wambui",
    ]
    for para in about_paragraphs:
        pdf.body(para)
        pdf.ln(1)

    pdf.output(OUT + "LinkedIn_Header_About_ShantelleWambuiKungu.pdf")
    print("v LinkedIn PDF generated")


# ══════════════════════════════════════════════════════════════════════════════
# 4. SELF REFLECTION
# ══════════════════════════════════════════════════════════════════════════════
def make_reflection():
    pdf = BasePDF("Week 11 Self-Reflection")
    pdf.add_page()

    pdf.set_fill_color(*NAVY)
    pdf.rect(0, 0, 210, 38, "F")
    pdf.set_xy(18, 8)
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(*WHITE)
    pdf.cell(0, 8, "Mock Interview Self-Reflection",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(18, 18)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 6, "Week 11  |  Shantelle Wambui Kungu  |  September 2026",
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_y(46)
    pdf.set_text_color(*BLACK)

    pdf.section_heading("REFLECTION")
    reflection = (
        "The mock interview pushed me to articulate decisions I had made instinctively during "
        "development. When asked 'why XGBoost over a neural network for ClaimGuard?', I had the "
        "right answer - interpretability requirements, tabular data structure, training data size "
        "- but I reached for it too slowly. That hesitation signals I need to practise verbalising "
        "technical trade-offs under pressure, not just know them.\n\n"

        "What went well: STAR responses for behavioural questions felt natural. When asked about "
        "a challenge I overcame, I described the SHAP NumPy 2.x compatibility issue clearly - "
        "problem, diagnosis, fix, lesson - without rambling. The interviewers noted the answer "
        "was specific and credible, which gave me confidence mid-session.\n\n"

        "Where I need to improve: quantifying impact on the first attempt. I initially described "
        "ClaimGuard as 'reducing manual review time significantly' before being prompted to give "
        "a number. The number - 95% reduction, from 5-15 days to under 30 seconds - is "
        "compelling. I should lead with it, not arrive at it after a follow-up question.\n\n"

        "My focus for real interviews: open every answer with the outcome, then explain the "
        "method. Numbers first. Narrative second. That order respects the interviewer's time "
        "and signals executive-level communication from the start."
    )
    pdf.body(reflection, size=11)

    pdf.ln(4)
    pdf.section_heading("KEY TAKEAWAYS")
    takeaways = [
        "Lead with quantified outcomes - 95% reduction, 28-day payback, AUC-ROC 0.84",
        "Practise technical trade-off explanations out loud, not just internally",
        "STAR structure is working - continue using it for all behavioural questions",
        "Slow down on the first sentence; rushing signals nerves more than the content does",
    ]
    for t in takeaways:
        pdf.bullet(t, size=11)

    pdf.output(OUT + "Week11_Self_Reflection_ShantelleWambuiKungu.pdf")
    print("v Self-Reflection generated")


# ── Run all ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    make_cv()
    make_business_case()
    make_linkedin()
    make_reflection()
    print("\nAll 4 PDFs saved to", OUT)
