"""
convert_pitch_to_pdf.py
Rebuilds the pitch deck directly as a PDF using ReportLab.
Output: Week11_Pitch_Deck_ShantelleWambuiKungu.pdf
"""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

OUT = "/home/shantel/week11_strategic_portfolio/Week11_Pitch_Deck_ShantelleWambuiKungu.pdf"

W, H = landscape(A4)   # 841.9 x 595.3 points

# Colours
NAVY   = HexColor("#0F172A")
ACCENT = HexColor("#10B981")
WHITE  = colors.white
LGREY  = HexColor("#94A3B8")
DGREY  = HexColor("#1E293B")
RED    = HexColor("#EF4444")
GREEN  = HexColor("#22C55E")
AMBER  = HexColor("#F59E0B")
CARD   = HexColor("#1E2D40")


def new_slide(c):
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def footer(c, text="Shantelle Wambui Kungu  |  PLP AI/ML Capstone  |  2026"):
    c.setFillColor(LGREY)
    c.setFont("Helvetica", 8)
    c.drawCentredString(W / 2, 18, text)


def slide_num(c, n):
    c.setFillColor(LGREY)
    c.setFont("Helvetica", 8)
    c.drawRightString(W - 20, 18, str(n))


def accent_bar(c, y, width=220):
    c.setFillColor(ACCENT)
    c.rect(40, y, width, 3, fill=1, stroke=0)


def heading(c, text, y, size=28):
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", size)
    c.drawString(40, y, text)


def sub(c, text, y, size=14, color=None):
    c.setFillColor(color or ACCENT)
    c.setFont("Helvetica-Bold", size)
    c.drawString(40, y, text)


def body_text(c, text, x, y, size=11, color=None, width=760):
    c.setFillColor(color or WHITE)
    c.setFont("Helvetica", size)
    # simple word wrap
    words = text.split()
    line = ""
    lines = []
    for word in words:
        test = (line + " " + word).strip()
        if c.stringWidth(test, "Helvetica", size) < width:
            line = test
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    for i, l in enumerate(lines):
        c.drawString(x, y - i * (size + 3), l)
    return y - len(lines) * (size + 3)


def card(c, x, y, w, h, fill=CARD):
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, 6, fill=1, stroke=0)


def kpi_boxes(c, items, y):
    bw = (W - 80) / len(items)
    clrs = [GREEN, ACCENT, AMBER]
    for i, (label, val) in enumerate(items):
        x = 40 + i * bw
        card(c, x, y, bw - 8, 50, fill=DGREY)
        c.setFillColor(clrs[i % 3])
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(x + (bw - 8) / 2, y + 28, val)
        c.setFillColor(LGREY)
        c.setFont("Helvetica", 9)
        c.drawCentredString(x + (bw - 8) / 2, y + 12, label)


# ─────────────────────────────────────────────────────────────────────────────
c = canvas.Canvas(OUT, pagesize=landscape(A4))
c.setTitle("ClaimGuard - Board Pitch")

# ══ SLIDE 1 — Title ══════════════════════════════════════════════════════════
new_slide(c)
c.setFillColor(ACCENT)
c.rect(0, H - 8, W, 8, fill=1, stroke=0)
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 56)
c.drawCentredString(W / 2, H - 110, "ClaimGuard")
c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(W / 2, H - 145, "AI-Powered Insurance Fraud Detection for the Kenyan Motor Market")
c.setFillColor(LGREY)
c.setFont("Helvetica", 3)
c.rect(200, H - 170, W - 400, 1, fill=1, stroke=0)
c.setFont("Helvetica", 13)
c.drawCentredString(W / 2, H - 190, "Shantelle Wambui Kungu  |  PLP AI/ML Capstone  |  September 2026")
c.setFillColor(LGREY)
c.setFont("Helvetica-Oblique", 11)
c.drawCentredString(W / 2, H - 260,
    '"The technology works. The numbers justify it. Today I\'m asking for the go-ahead."')
c.setFillColor(ACCENT)
c.rect(0, 0, W, 6, fill=1, stroke=0)
c.showPage()

# ══ SLIDE 2 — Problem ════════════════════════════════════════════════════════
new_slide(c)
heading(c, "The Problem", H - 70)
accent_bar(c, H - 78)
sub(c, "KES 40-60 Billion Lost to Motor Insurance Fraud Every Year", H - 105)

data = [
    ("5-15 days",   "Manual review takes 5-15 days per claim -- adjusters catch only 40% of fraud"),
    ("60% missed",  "Organised fraud rings file across multiple policyholders -- invisible to a single reviewer"),
    ("KES 14.4M",   "A mid-size insurer loses approximately KES 14.4M in undetected fraud every month"),
]
for i, (stat, text) in enumerate(data):
    y = H - 175 - i * 95
    card(c, 40, y, 130, 70, fill=HexColor("#7F1D1D"))
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(105, y + 30, stat)
    card(c, 180, y, W - 220, 70, fill=CARD)
    body_text(c, text, 195, y + 42, size=12, width=580)

card(c, 40, 35, W - 80, 30, fill=DGREY)
c.setFillColor(ACCENT)
c.setFont("Helvetica-Oblique", 11)
c.drawCentredString(W / 2, 47, "The problem isn't that fraud happens. It's that 60% of it goes undetected.")
footer(c); slide_num(c, 2); c.showPage()

# ══ SLIDE 3 — Cost of Inaction ═══════════════════════════════════════════════
new_slide(c)
heading(c, "Cost of Inaction", H - 70)
accent_bar(c, H - 78)
sub(c, "What This Costs Every Month -- Without ClaimGuard", H - 105)

rows = [
    ("Undetected fraud",            "160 claims x KES 150K x 60% missed",         "KES 14.4M"),
    ("Adjuster false-positive rework", "40% wrongly flagged x rework cost",        "KES 1.6M"),
    ("TOTAL VISIBLE MONTHLY LOSS",  "",                                             "~KES 16M"),
]
col_x = [40, 310, 670]
col_w = [265, 355, 130]
# header
for j, (h, x, w) in enumerate(zip(["Item", "Calculation", "Monthly Loss"], col_x, col_w)):
    card(c, x, H - 160, w - 4, 28, fill=HexColor("#1E406B"))
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + (w - 4) / 2, H - 149, h)

for i, (item, calc, loss) in enumerate(rows):
    y = H - 200 - i * 55
    is_total = i == 2
    bg = HexColor("#14532D") if is_total else CARD
    fc = GREEN if is_total else WHITE
    for text, x, w in zip([item, calc, loss], col_x, col_w):
        card(c, x, y, w - 4, 44, fill=bg)
        c.setFillColor(fc)
        c.setFont("Helvetica-Bold" if is_total else "Helvetica", 10)
        c.drawCentredString(x + (w - 4) / 2, y + 16, text)

card(c, 40, 35, W - 80, 32, fill=HexColor("#7F1D1D"))
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 11)
c.drawCentredString(W / 2, 48, "Every month we delay costs the business approximately KES 16 million.")
footer(c); slide_num(c, 3); c.showPage()

# ══ SLIDE 4 — Solution ═══════════════════════════════════════════════════════
new_slide(c)
heading(c, "Our Solution", H - 70)
accent_bar(c, H - 78)
sub(c, "ClaimGuard: Three Layers of Intelligence", H - 105)

# Pipeline flow
steps = ["Claim\nArrives", "Rules\nEngine", "ML\nScorer", "Network\nDetector", "Auto\nRoute"]
sw = 130
for i, step in enumerate(steps):
    x = 40 + i * 156
    card(c, x, H - 175, sw, 45, fill=HexColor("#1E406B"))
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 11)
    for j, line in enumerate(step.split("\n")):
        c.drawCentredString(x + sw / 2, H - 148 + (1 - j) * 14, line)
    if i < 4:
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(x + sw + 8, H - 158, ">")

# 3 detail cards
details = [
    ("Rules Engine",
     ["8 hard fraud rules:", "* Claim within 14 days of inception", "* Duplicate OB numbers",
      "* Provider billing spikes", "* Round-sum amounts, missing docs"]),
    ("XGBoost ML Scorer",
     ["25 engineered features", "Fraud probability: 0 to 1", "",
      "AUC-ROC:  0.84", "Precision: 79%   Recall: 81%"]),
    ("Network / Ring Detector",
     ["Graph analysis across providers,", "claimants, and vehicles.", "",
      "Detects organised rings", "invisible to human reviewers."]),
]
for i, (title, lines) in enumerate(details):
    x = 40 + i * 266
    card(c, x, 65, 255, 195, fill=CARD)
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x + 10, 240, title)
    c.setFillColor(WHITE)
    c.setFont("Helvetica", 10)
    for j, line in enumerate(lines):
        c.drawString(x + 10, 220 - j * 17, line)

footer(c); slide_num(c, 4); c.showPage()

# ══ SLIDE 5 — Results ════════════════════════════════════════════════════════
new_slide(c)
heading(c, "Results", H - 70)
accent_bar(c, H - 78)
sub(c, "What ClaimGuard Delivers", H - 105)

metrics = [
    ("Processing Time",         "5-15 days",    "< 30 seconds",     "99.7% faster"),
    ("Fraud Detection Rate",    "40%",           "81%",              "+41 percentage points"),
    ("Fraud Rings Found",       "0 (invisible)", "12 rings",         "KES 4.2M surfaced"),
    ("Manual Review Workload",  "100%",          "5% (oversight)",   "95% reduction"),
]
hdrs = ["Metric", "Manual", "ClaimGuard", "Improvement"]
col_x2 = [40, 260, 430, 600]
col_w2 = [215, 165, 165, 200]

for j, (h, x, w) in enumerate(zip(hdrs, col_x2, col_w2)):
    card(c, x, H - 160, w - 4, 28, fill=HexColor("#1E406B"))
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + (w - 4) / 2, H - 149, h)

for i, (metric, manual, cg, imp) in enumerate(metrics):
    y = H - 200 - i * 60
    row = [metric, manual, cg, imp]
    for j, (text, x, w) in enumerate(zip(row, col_x2, col_w2)):
        bg = HexColor("#14532D") if j == 2 else CARD
        fc = GREEN if j == 2 else (AMBER if j == 3 else WHITE)
        card(c, x, y, w - 4, 48, fill=bg)
        c.setFillColor(fc)
        c.setFont("Helvetica-Bold" if j == 2 else "Helvetica", 11)
        c.drawCentredString(x + (w - 4) / 2, y + 18, text)

footer(c); slide_num(c, 5); c.showPage()

# ══ SLIDE 6 — Business Case ══════════════════════════════════════════════════
new_slide(c)
heading(c, "The Business Case", H - 70)
accent_bar(c, H - 78)
sub(c, "The Numbers That Matter to This Room", H - 105)

# Savings table (left)
card(c, 40, 90, 370, 270, fill=CARD)
c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 12)
c.drawString(55, 342, "Annual Savings")
savings = [
    ("Additional fraud caught",    "KES 118.1M"),
    ("Adjuster time savings",      "KES 10.9M"),
    ("False positive reduction",   "KES 19.2M"),
    ("TOTAL ANNUAL SAVINGS",       "KES 148.2M"),
]
for i, (label, val) in enumerate(savings):
    y = 315 - i * 48
    is_t = i == 3
    c.setFillColor(GREEN if is_t else WHITE)
    c.setFont("Helvetica-Bold" if is_t else "Helvetica", 10)
    c.drawString(55, y, label)
    c.drawRightString(395, y, val)

# Investment table (right)
card(c, 430, 90, 370, 270, fill=CARD)
c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 12)
c.drawString(445, 342, "Year 1 Investment")
costs = [
    ("Development & integration",  "KES 8.5M"),
    ("Cloud infrastructure",       "KES 1.8M"),
    ("Maintenance & retraining",   "KES 1.2M"),
    ("TOTAL INVESTMENT",           "KES 11.5M"),
]
for i, (label, val) in enumerate(costs):
    y = 315 - i * 48
    is_t = i == 3
    c.setFillColor(AMBER if is_t else WHITE)
    c.setFont("Helvetica-Bold" if is_t else "Helvetica", 10)
    c.drawString(445, y, label)
    c.drawRightString(785, y, val)

kpi_boxes(c, [("Year 1 ROI", "1,188%"), ("Payback Period", "28 Days"), ("5-Year NPV", "KES 580M")], 32)
footer(c); slide_num(c, 6); c.showPage()

# ══ SLIDE 7 — Risks ══════════════════════════════════════════════════════════
new_slide(c)
heading(c, "Risks & Mitigation", H - 70)
accent_bar(c, H - 78)
sub(c, "We've Thought About What Can Go Wrong", H - 105)

risk_data = [
    ("Risk 1: Regulatory Challenge",
     "IRA or a policyholder challenges an automated rejection",
     "Every rejection includes a full SHAP audit trail. Human review is mandatory for all "
     "rejections. Designed to comply with IRA data governance guidelines."),
    ("Risk 2: Model Drift",
     "Fraud patterns evolve faster than the model retrains",
     "Automated monthly retraining with champion/challenger model registry. Alert fires "
     "if AUC-ROC drops below 0.78, triggering immediate retraining."),
]
for i, (title, risk, mit) in enumerate(risk_data):
    y = H - 200 - i * 150
    card(c, 40, y, 220, 115, fill=HexColor("#7F1D1D"))
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(55, y + 90, title)
    c.setFillColor(LGREY)
    c.setFont("Helvetica", 9)
    body_text(c, risk, 55, y + 72, size=9, color=LGREY, width=190)

    card(c, 275, y, W - 315, 115, fill=HexColor("#14532D"))
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(290, y + 90, "Mitigation")
    body_text(c, mit, 290, y + 72, size=10, color=WHITE, width=510)

footer(c); slide_num(c, 7); c.showPage()

# ══ SLIDE 8 — Tech Ready ══════════════════════════════════════════════════════
new_slide(c)
heading(c, "The Technology Is Ready", H - 70)
accent_bar(c, H - 78)
sub(c, "This Is Not a Proposal. It's a Deployed System.", H - 105)

checklist = [
    ("Backend",      "Python/FastAPI -- production-grade, containerised with Docker"),
    ("Database",     "PostgreSQL -- 22-table schema, migrations managed with Alembic"),
    ("ML Pipeline",  "XGBoost trainer, SHAP explainer, model registry with promote/rollback"),
    ("Frontend",     "Next.js -- case review, HITL queue, network visualisation, ML admin"),
    ("Security",     "JWT auth, 8 user roles, full audit trail on every single decision"),
    ("Scalability",  "Celery + Redis async processing, horizontal scaling ready"),
]
for i, (component, detail) in enumerate(checklist):
    y = H - 155 - i * 58
    card(c, 40, y, W - 80, 46, fill=CARD)
    c.setFillColor(GREEN)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(55, y + 16, "v")
    c.setFillColor(ACCENT)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(80, y + 16, component)
    c.setFillColor(WHITE)
    c.setFont("Helvetica", 10)
    c.drawString(230, y + 16, detail)

footer(c); slide_num(c, 8); c.showPage()

# ══ SLIDE 9 — The Ask ════════════════════════════════════════════════════════
new_slide(c)
heading(c, "What We're Asking For", H - 70)
accent_bar(c, H - 78)
sub(c, "Three Approvals. One Decision.", H - 105)

asks = [
    ("1", "Budget: KES 11.5M (Year 1)",
     "Development & integration sprint\nCloud infrastructure\nCompliance review", GREEN),
    ("2", "IT Window: Q4 2026",
     "90-day integration with InsureMaster\nZero disruption to existing systems", ACCENT),
    ("3", "Compliance Sign-off",
     "IRA data governance review\nFull documentation provided", AMBER),
]
bw = (W - 80) / 3
for i, (num, title, body, clr) in enumerate(asks):
    x = 40 + i * (bw + 5)
    card(c, x, 65, bw - 5, 310, fill=CARD)
    c.setFillColor(clr)
    c.rect(x, 355, bw - 5, 6, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 42)
    c.drawCentredString(x + (bw - 5) / 2, 290, num)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(x + (bw - 5) / 2, 255, title)
    c.setFillColor(LGREY)
    c.setFont("Helvetica", 10)
    for j, line in enumerate(body.split("\n")):
        c.drawCentredString(x + (bw - 5) / 2, 220 - j * 22, line)

footer(c); slide_num(c, 9); c.showPage()

# ══ SLIDE 10 — Close ══════════════════════════════════════════════════════════
new_slide(c)
c.setFillColor(ACCENT)
c.rect(0, H - 6, W, 6, fill=1, stroke=0)
c.rect(0, 0, W, 6, fill=1, stroke=0)

c.setFillColor(ACCENT)
c.setFont("Helvetica-Bold", 90)
c.drawCentredString(W / 2, H - 140, "Go.")

c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 40)
c.drawCentredString(W / 2, H - 195, "Deploy ClaimGuard.")

lines = [
    ("KES 11.5M investment.", LGREY),
    ("KES 148M return in Year 1.", WHITE),
    ("Payback in 28 days.", WHITE),
    ("The technology works.", ACCENT),
]
for i, (line, clr) in enumerate(lines):
    c.setFillColor(clr)
    c.setFont("Helvetica", 18)
    c.drawCentredString(W / 2, H - 260 - i * 32, line)

c.setFillColor(LGREY)
c.setFont("Helvetica-Oblique", 16)
c.drawCentredString(W / 2, 100, "Questions?")

c.setFillColor(LGREY)
c.setFont("Helvetica", 9)
c.drawCentredString(W / 2, 30,
    "Shantelle Wambui Kungu  |  shantellewambuikungu@gmail.com  |  github.com/Shantelle-wambui")
c.showPage()

c.save()
print(f"Saved -> {OUT}")
