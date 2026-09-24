"""
generate_pitch_deck.py
Generates Week11_Pitch_Deck_ShantelleWambuiKungu.pptx
Run: python generate_pitch_deck.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# ── Colour palette ────────────────────────────────────────────────────────────
DARK_BG     = RGBColor(0x0F, 0x17, 0x2A)   # deep navy
ACCENT      = RGBColor(0x6E, 0xE7, 0xB7)   # mint green
ACCENT2     = RGBColor(0xF5, 0x9E, 0x0B)   # amber
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GREY  = RGBColor(0xCB, 0xD5, 0xE1)
RED         = RGBColor(0xEF, 0x44, 0x44)
GREEN       = RGBColor(0x22, 0xC5, 0x5E)
CARD_BG     = RGBColor(0x1E, 0x2D, 0x40)   # slightly lighter navy for cards

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

BLANK = prs.slide_layouts[6]  # fully blank layout

# ── Helper functions ──────────────────────────────────────────────────────────

def add_slide():
    slide = prs.slides.add_slide(BLANK)
    # Dark background
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = DARK_BG
    return slide


def txb(slide, text, x, y, w, h,
        size=18, bold=False, color=WHITE, align=PP_ALIGN.LEFT,
        italic=False, wrap=True):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.italic = italic
    return tb


def rect(slide, x, y, w, h, fill_color=CARD_BG, line_color=None):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(x), Inches(y), Inches(w), Inches(h)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(1)
    else:
        shape.line.fill.background()
    return shape


def accent_bar(slide, y=1.15):
    """Thin horizontal accent line under headings."""
    shape = slide.shapes.add_shape(1, Inches(0.5), Inches(y), Inches(3), Inches(0.04))
    shape.fill.solid()
    shape.fill.fore_color.rgb = ACCENT
    shape.line.fill.background()


def footer(slide, name="Shantelle Wambui Kungu  |  PLP AI/ML Capstone  |  2026"):
    txb(slide, name, 0.3, 7.1, 12.7, 0.35, size=9, color=LIGHT_GREY, align=PP_ALIGN.CENTER)


def slide_number(slide, n):
    txb(slide, str(n), 12.8, 7.1, 0.4, 0.35, size=9, color=LIGHT_GREY, align=PP_ALIGN.RIGHT)


# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()

# Big logo-style rectangle
r = rect(s, 0.5, 0.4, 12.33, 0.08, fill_color=ACCENT)

txb(s, "ClaimGuard", 0.5, 0.6, 12, 1.6,
    size=72, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

txb(s, "AI-Powered Insurance Fraud Detection for the Kenyan Motor Market",
    0.5, 2.3, 12.33, 0.8, size=24, color=ACCENT, align=PP_ALIGN.CENTER)

rect(s, 3.2, 3.4, 6.9, 0.04, fill_color=LIGHT_GREY)

txb(s, "Shantelle Wambui Kungu  |  PLP AI/ML Capstone  |  September 2026",
    0.5, 3.6, 12.33, 0.5, size=16, color=LIGHT_GREY, align=PP_ALIGN.CENTER)

txb(s, '"The technology works. The numbers justify it. Today I\'m asking for the go-ahead."',
    1.0, 5.0, 11.33, 0.8, size=14, italic=True, color=LIGHT_GREY, align=PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — The Problem
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "The Problem", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "KES 40–60 Billion Lost to Motor Insurance Fraud Every Year",
    0.5, 1.25, 12, 0.55, size=20, color=ACCENT, bold=True)

bullets = [
    ("5–15 days",    "Manual review takes 5–15 days per claim — adjusters catch only 40% of fraud"),
    ("60% missed",   "Organised fraud rings file across multiple policyholders — invisible to a single reviewer"),
    ("KES 14.4M",    "A mid-size insurer loses approximately KES 14.4M in undetected fraud every month"),
]
for i, (stat, text) in enumerate(bullets):
    y = 2.1 + i * 1.3
    rect(s, 0.5, y, 2.2, 1.0, fill_color=RGBColor(0x7F, 0x1D, 0x1D))
    txb(s, stat, 0.5, y + 0.2, 2.2, 0.6, size=22, bold=True, color=RED, align=PP_ALIGN.CENTER)
    rect(s, 2.85, y, 9.8, 1.0, fill_color=CARD_BG)
    txb(s, text, 3.0, y + 0.2, 9.5, 0.6, size=16, color=WHITE)

rect(s, 0.5, 6.0, 12.33, 0.7, fill_color=RGBColor(0x1A, 0x1A, 0x2E))
txb(s, "The problem isn't that fraud happens. It's that 60% of it goes undetected.",
    0.7, 6.05, 11.9, 0.6, size=15, italic=True, color=ACCENT, align=PP_ALIGN.CENTER)
footer(s); slide_number(s, 2)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — Cost of Inaction
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "Cost of Inaction", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "What This Costs Every Month — Without ClaimGuard",
    0.5, 1.25, 12, 0.5, size=20, color=ACCENT, bold=True)

rows = [
    ("Undetected fraud",            "160 claims × KES 150K × 60% missed",     "KES 14.4M"),
    ("Adjuster false-positive rework", "40% wrongly flagged × rework cost",   "KES 1.6M"),
    ("Total visible monthly loss",  "",                                         "~KES 16M"),
]
headers = ["Item", "Calculation", "Monthly Loss"]
col_w = [4.5, 5.5, 2.2]
col_x = [0.5, 5.1, 10.7]
# header row
for j, (h, w, x) in enumerate(zip(headers, col_w, col_x)):
    rect(s, x, 2.0, w - 0.05, 0.5, fill_color=RGBColor(0x1E, 0x40, 0x6B))
    txb(s, h, x + 0.1, 2.05, w - 0.2, 0.4, size=13, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)

for i, (item, calc, loss) in enumerate(rows):
    y = 2.6 + i * 0.9
    is_total = i == 2
    bg = RGBColor(0x14, 0x53, 0x2D) if is_total else CARD_BG
    fc = GREEN if is_total else WHITE
    for j, (text, w, x) in enumerate(zip([item, calc, loss], col_w, col_x)):
        rect(s, x, y, w - 0.05, 0.8, fill_color=bg)
        txb(s, text, x + 0.1, y + 0.15, w - 0.2, 0.5,
            size=14, bold=is_total, color=fc, align=PP_ALIGN.CENTER)

rect(s, 0.5, 5.9, 12.33, 0.8, fill_color=RGBColor(0x7F, 0x1D, 0x1D))
txb(s, "Every month we delay costs the business approximately KES 16 million in avoidable losses.",
    0.7, 6.0, 11.9, 0.6, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
footer(s); slide_number(s, 3)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — Our Solution
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "Our Solution", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "ClaimGuard: Three Layers of Intelligence",
    0.5, 1.25, 12, 0.5, size=20, color=ACCENT, bold=True)

# Pipeline flow
steps = ["Claim\nArrives", "Rules\nEngine", "ML\nScorer", "Network\nDetector", "Auto\nRoute"]
for i, step in enumerate(steps):
    x = 0.5 + i * 2.5
    rect(s, x, 2.1, 2.1, 0.85, fill_color=RGBColor(0x1E, 0x40, 0x6B))
    txb(s, step, x, 2.15, 2.1, 0.75, size=13, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
    if i < 4:
        txb(s, "→", x + 2.1, 2.3, 0.35, 0.5, size=22, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

# 3 detail cards
cards = [
    ("Rules Engine",
     "8 hard fraud rules:\n• Claim within 14 days of inception\n• Duplicate OB numbers\n• Provider billing spikes\n• Round-sum amounts\n• Missing documents"),
    ("XGBoost ML Scorer",
     "25 engineered features → fraud probability 0–1\n\nAUC-ROC  0.84\nPrecision  79%\nRecall  81%"),
    ("Network / Ring Detector",
     "Graph analysis across providers,\nclaimants, and vehicles.\n\nDetects organised rings invisible\nto human reviewers."),
]
for i, (title, body) in enumerate(cards):
    x = 0.5 + i * 4.3
    rect(s, x, 3.3, 4.1, 3.1, fill_color=CARD_BG)
    txb(s, title, x + 0.1, 3.35, 3.9, 0.45, size=14, bold=True, color=ACCENT)
    txb(s, body, x + 0.1, 3.85, 3.9, 2.4, size=12, color=WHITE)

footer(s); slide_number(s, 4)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — Results
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "Results", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "What ClaimGuard Delivers",
    0.5, 1.25, 12, 0.5, size=20, color=ACCENT, bold=True)

metrics = [
    ("Processing Time",        "5–15 days",  "< 30 seconds",   "99.7% faster"),
    ("Fraud Detection Rate",   "40%",         "81%",            "+41 percentage points"),
    ("Fraud Rings Found",      "0 (invisible)", "12 rings",      "KES 4.2M exposure surfaced"),
    ("Manual Review Workload", "100%",        "5% (oversight)", "95% reduction"),
]
headers2 = ["Metric", "Manual Process", "ClaimGuard", "Improvement"]
col_w2 = [3.3, 2.6, 2.6, 3.5]
col_x2 = [0.4, 3.8, 6.5, 9.2]

for j, (h, w, x) in enumerate(zip(headers2, col_w2, col_x2)):
    rect(s, x, 2.05, w - 0.05, 0.5, fill_color=RGBColor(0x1E, 0x40, 0x6B))
    txb(s, h, x + 0.1, 2.1, w - 0.2, 0.4, size=13, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)

for i, (metric, manual, cg, improvement) in enumerate(metrics):
    y = 2.65 + i * 0.9
    row_data = [metric, manual, cg, improvement]
    for j, (text, w, x) in enumerate(zip(row_data, col_w2, col_x2)):
        bg = RGBColor(0x14, 0x53, 0x2D) if j == 2 else CARD_BG
        fc = GREEN if j == 2 else (ACCENT2 if j == 3 else WHITE)
        rect(s, x, y, w - 0.05, 0.8, fill_color=bg)
        txb(s, text, x + 0.1, y + 0.15, w - 0.2, 0.5,
            size=13, bold=(j == 2), color=fc, align=PP_ALIGN.CENTER)

footer(s); slide_number(s, 5)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Business Case / ROI
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "The Business Case", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "The Numbers That Matter to This Room",
    0.5, 1.25, 12, 0.5, size=20, color=ACCENT, bold=True)

# Left — savings
rect(s, 0.4, 2.0, 5.8, 3.5, fill_color=CARD_BG)
txb(s, "Annual Savings", 0.5, 2.05, 5.6, 0.45, size=15, bold=True, color=ACCENT)
savings = [
    ("Additional fraud caught",      "KES 118.1M"),
    ("Adjuster time savings",        "KES 10.9M"),
    ("False positive reduction",     "KES 19.2M"),
    ("TOTAL ANNUAL SAVINGS",         "KES 148.2M"),
]
for i, (label, val) in enumerate(savings):
    y = 2.6 + i * 0.7
    is_total = i == 3
    txb(s, label, 0.5, y, 3.5, 0.6, size=13, bold=is_total,
        color=ACCENT if is_total else WHITE)
    txb(s, val,   3.8, y, 2.2, 0.6, size=13, bold=is_total,
        color=GREEN if is_total else LIGHT_GREY, align=PP_ALIGN.RIGHT)

# Right — investment
rect(s, 6.5, 2.0, 5.8, 3.5, fill_color=CARD_BG)
txb(s, "Year 1 Investment", 6.6, 2.05, 5.6, 0.45, size=15, bold=True, color=ACCENT)
costs = [
    ("Development & integration",  "KES 8.5M"),
    ("Cloud infrastructure",       "KES 1.8M"),
    ("Maintenance & retraining",   "KES 1.2M"),
    ("TOTAL INVESTMENT",           "KES 11.5M"),
]
for i, (label, val) in enumerate(costs):
    y = 2.6 + i * 0.7
    is_total = i == 3
    txb(s, label, 6.6, y, 3.5, 0.6, size=13, bold=is_total,
        color=ACCENT if is_total else WHITE)
    txb(s, val,   9.9, y, 2.2, 0.6, size=13, bold=is_total,
        color=ACCENT2 if is_total else LIGHT_GREY, align=PP_ALIGN.RIGHT)

# ROI highlight boxes
kpis = [("ROI: 1,188%", GREEN), ("Payback: 28 Days", ACCENT), ("5-Yr NPV: KES 580M", ACCENT2)]
for i, (label, color) in enumerate(kpis):
    x = 0.4 + i * 4.15
    rect(s, x, 5.75, 3.9, 0.9, fill_color=RGBColor(0x0A, 0x0F, 0x1E))
    txb(s, label, x, 5.8, 3.9, 0.8, size=18, bold=True, color=color, align=PP_ALIGN.CENTER)

footer(s); slide_number(s, 6)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 7 — Risks & Mitigation
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "Risks & Mitigation", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "We've Thought About What Can Go Wrong",
    0.5, 1.25, 12, 0.5, size=20, color=ACCENT, bold=True)

risks = [
    (
        "Risk 1: Regulatory Challenge",
        "IRA or a policyholder challenges an automated rejection",
        "Every rejection includes a full SHAP audit trail explaining the decision in plain English. "
        "Human review is mandatory for all rejections. Designed from the ground up to comply with "
        "IRA data governance guidelines.",
    ),
    (
        "Risk 2: Model Drift",
        "Fraud patterns evolve faster than the model retrains",
        "Automated monthly retraining pipeline with a champion/challenger model registry. "
        "Performance alert fires if AUC-ROC drops below 0.78, triggering immediate review "
        "and retraining.",
    ),
]
for i, (title, risk_text, mitigation) in enumerate(risks):
    y = 2.1 + i * 2.3
    rect(s, 0.4, y, 3.5, 2.0, fill_color=RGBColor(0x7F, 0x1D, 0x1D))
    txb(s, title, 0.5, y + 0.1, 3.3, 0.5, size=14, bold=True, color=RED)
    txb(s, risk_text, 0.5, y + 0.65, 3.3, 1.2, size=12, color=LIGHT_GREY)
    rect(s, 4.1, y, 8.6, 2.0, fill_color=RGBColor(0x14, 0x53, 0x2D))
    txb(s, "✅  Mitigation", 4.2, y + 0.1, 8.3, 0.45, size=14, bold=True, color=GREEN)
    txb(s, mitigation, 4.2, y + 0.6, 8.3, 1.3, size=12, color=WHITE)

footer(s); slide_number(s, 7)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 8 — Technology is Ready
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "The Technology Is Ready", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "This Is Not a Proposal. It's a Deployed System.",
    0.5, 1.25, 12, 0.5, size=20, color=ACCENT, bold=True)

checklist = [
    ("Backend", "Python/FastAPI — production-grade, containerised with Docker"),
    ("Database", "PostgreSQL — 22-table schema, migrations managed with Alembic"),
    ("ML Pipeline", "XGBoost trainer, SHAP explainer, model registry with promote/rollback"),
    ("Frontend", "Next.js — case review, HITL queue, network visualisation, ML admin portal"),
    ("Security", "JWT auth, 8 user roles, full audit trail on every single decision"),
    ("Scalability", "Celery + Redis async processing, horizontal scaling ready"),
]
for i, (component, detail) in enumerate(checklist):
    y = 2.05 + i * 0.8
    rect(s, 0.4, y, 12.4, 0.72, fill_color=CARD_BG)
    txb(s, "✅", 0.5, y + 0.12, 0.5, 0.5, size=16, color=GREEN)
    txb(s, component, 1.1, y + 0.12, 2.2, 0.5, size=14, bold=True, color=ACCENT)
    txb(s, detail, 3.4, y + 0.12, 9.2, 0.5, size=13, color=WHITE)

rect(s, 0.4, 6.95, 12.4, 0.12, fill_color=ACCENT)
txb(s, "The only thing missing is production data and your authorisation to connect to InsureMaster.",
    0.4, 6.9, 12.4, 0.4, size=13, italic=True, color=LIGHT_GREY, align=PP_ALIGN.CENTER)
footer(s); slide_number(s, 8)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 9 — The Ask
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()
accent_bar(s)
txb(s, "What We're Asking For", 0.5, 0.3, 12, 0.7, size=36, bold=True, color=WHITE)
txb(s, "Three Approvals. One Decision.",
    0.5, 1.25, 12, 0.5, size=20, color=ACCENT, bold=True)

asks = [
    ("1", "Budget: KES 11.5M (Year 1)",
     "Development & integration sprint\nCloud infrastructure\nCompliance review",
     GREEN),
    ("2", "IT Window: Q4 2026",
     "90-day integration with InsureMaster\nZero disruption to existing systems",
     ACCENT),
    ("3", "Compliance Sign-off",
     "IRA data governance review\nFull documentation provided",
     ACCENT2),
]
for i, (num, title, body, color) in enumerate(asks):
    x = 0.4 + i * 4.2
    rect(s, x, 2.2, 3.9, 4.5, fill_color=CARD_BG)
    rect(s, x, 2.2, 3.9, 0.1, fill_color=color)
    txb(s, num, x, 2.4, 3.9, 0.9, size=48, bold=True, color=color, align=PP_ALIGN.CENTER)
    txb(s, title, x + 0.1, 3.4, 3.7, 0.7, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txb(s, body, x + 0.15, 4.2, 3.6, 2.3, size=13, color=LIGHT_GREY, align=PP_ALIGN.CENTER)

footer(s); slide_number(s, 9)

# ══════════════════════════════════════════════════════════════════════════════
# SLIDE 10 — Close
# ══════════════════════════════════════════════════════════════════════════════
s = add_slide()

# Full-width accent bar at top
rect(s, 0, 0, 13.33, 0.12, fill_color=ACCENT)

txb(s, "Go.", 0.5, 0.5, 12.33, 1.4,
    size=96, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
txb(s, "Deploy ClaimGuard.", 0.5, 1.9, 12.33, 1.1,
    size=48, bold=True, color=WHITE, align=PP_ALIGN.CENTER)

lines = [
    ("KES 11.5M investment.",    LIGHT_GREY),
    ("KES 148M return in Year 1.",  WHITE),
    ("Payback in 28 days.",         WHITE),
    ("The technology works.",        ACCENT),
]
for i, (line, color) in enumerate(lines):
    txb(s, line, 0.5, 3.3 + i * 0.65, 12.33, 0.6,
        size=22, color=color, align=PP_ALIGN.CENTER)

rect(s, 0, 7.38, 13.33, 0.12, fill_color=ACCENT)
txb(s, "Shantelle Wambui Kungu  |  shantellewambuikungu@gmail.com  |  github.com/Shantelle-wambui",
    0.5, 6.95, 12.33, 0.4, size=11, color=LIGHT_GREY, align=PP_ALIGN.CENTER)
txb(s, "Questions?", 0.5, 5.8, 12.33, 0.6,
    size=28, italic=True, color=LIGHT_GREY, align=PP_ALIGN.CENTER)

# ── Save ──────────────────────────────────────────────────────────────────────
out = "/home/shantel/week11_strategic_portfolio/Week11_Pitch_Deck_ShantelleWambuiKungu.pptx"
prs.save(out)
print(f"Saved → {out}")
