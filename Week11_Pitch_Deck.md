# Week11_Pitch_Deck — ClaimGuard Board Pitch
## 15-Minute Strategy Pitch | Shantelle Wambui Kungu | Week 11

---

## SLIDE 1 — TITLE (0:00–0:30)

# ClaimGuard
### AI-Powered Insurance Fraud Detection for the Kenyan Motor Market

**Shantelle Wambui Kungu**  
Data Analyst & AI/ML Engineer | PLP Capstone  
September 2026

*"We built the system. The numbers justify it. Today I'm asking for the go-ahead to deploy it."*

---

## SLIDE 2 — THE PROBLEM (0:30–2:00)

### KES 40–60 Billion Disappears Every Year

- Kenya's motor insurance sector loses **KES 40–60B annually** to fraud (IRA Kenya, 2024)
- Your adjusters review claims manually — taking **5 to 15 days per file**
- They catch only **40% of fraud** — because the other 60% is organised, cross-claim, and invisible to a single reviewer
- A garage can file 9 fraudulent claims across 9 different policyholders and no one connects the dots

**The question isn't whether you have a fraud problem.**  
**The question is how long you're willing to pay for it.**

---

## SLIDE 3 — THE COST RIGHT NOW (2:00–3:30)

### What Inaction Costs This Business Monthly

| Item | Calculation | Monthly Loss |
|---|---|---|
| Undetected fraud (mid-size insurer) | 160 fraudulent claims × KES 150K × 60% missed | **KES 14.4M** |
| Adjuster overhead on false positives | 40% wrongly flagged clean claims × rework cost | **KES 1.6M** |
| Reputational cost of delayed legit claims | Customer churn, regulatory friction | **Unquantified** |
| **Total visible monthly cost** | | **~KES 16M** |

> *Every month without ClaimGuard costs this business approximately KES 16 million.*

---

## SLIDE 4 — OUR SOLUTION (3:30–5:30)

### ClaimGuard: Three Layers of Intelligence

```
Claim Arrives → Rules Engine → ML Scorer → Network Detector → Route
```

**Layer 1 — Rules Engine**
- 8 hard business rules: claim within 14 days of inception, duplicate OB numbers,
  provider billing spikes, suspiciously round amounts, missing documents
- Instant hard-fail on clear violations

**Layer 2 — XGBoost ML Scorer**
- 25 engineered features per claim
- Outputs a 0–1 fraud probability score
- **AUC-ROC 0.84 | Precision 79% | Recall 81%**

**Layer 3 — Network / Ring Detector**
- Graph analysis across providers, claimants, and vehicles
- Identifies organised fraud rings invisible to individual reviewers
- Found 12 rings / KES 4.2M exposure in our test dataset

**Every decision comes with a plain-English SHAP explanation** — so adjusters understand *why*,
and regulators see a full audit trail.

---

## SLIDE 5 — LIVE DEMO RESULTS (5:30–7:00)

### What ClaimGuard Delivered on Real Test Data

| Metric | Manual Process | ClaimGuard | Improvement |
|---|---|---|---|
| Processing time | 5–15 days | **< 30 seconds** | **99.7% faster** |
| Fraud detection rate | 40% | **81%** | **+41 percentage points** |
| False positive rate | High | **21% lower** | Fewer clean claims delayed |
| Fraud rings found | 0 (invisible) | **12 rings** | KES 4.2M exposure surfaced |
| Adjusters needed | 8 full-time | **2 (oversight only)** | **75% headcount reduction** |

---

## SLIDE 6 — THE BUSINESS CASE (7:00–9:00)

### The Numbers That Matter to This Room

**Annual Savings (mid-size insurer, 2,000 claims/month)**

| Source | Monthly | Annual |
|---|---|---|
| Additional fraud caught | KES 9.84M | KES 118M |
| Adjuster time savings | KES 0.91M | KES 10.9M |
| False positive reduction | KES 1.60M | KES 19.2M |
| **Total** | **KES 12.35M** | **KES 148.2M** |

**Investment**

| Cost | Year 1 | Year 2+ |
|---|---|---|
| Development & integration | KES 8.5M | — |
| Cloud infrastructure | KES 1.8M | KES 1.8M |
| Maintenance & retraining | KES 1.2M | KES 1.2M |
| **Total** | **KES 11.5M** | **KES 3.0M** |

### ROI Summary

```
Year 1 ROI     = 1,188%
Payback Period = 28 days
5-Year NPV     = KES 580M (10% discount rate)
```

**This system pays for itself in under one month.**

---

## SLIDE 7 — RISKS & HOW WE HANDLE THEM (9:00–10:30)

### We've Thought About What Can Go Wrong

| Risk | Our Response |
|---|---|
| **Regulatory challenge** — IRA questions automated rejections | Every rejection includes a full SHAP audit trail. Human review is mandatory for all rejections. We comply with IRA data governance guidelines. |
| **Model drift** — Fraudsters adapt | Automated monthly retraining with a champion/challenger model registry. Alert fires if AUC-ROC drops below 0.78. |
| **Integration complexity** — InsureMaster API variability | We have already built the InsureMaster adapter in both live and faker modes. 90-day integration sprint is scoped. |

---

## SLIDE 8 — THE TECHNOLOGY IS READY (10:30–12:00)

### This Is Not a Proposal. It's a Deployed System.

✅ **Backend:** Python/FastAPI — production-grade, containerised with Docker  
✅ **Database:** PostgreSQL — 22-table schema, migrations managed with Alembic  
✅ **ML Pipeline:** XGBoost trainer, SHAP explainer, model registry with promote/rollback  
✅ **Frontend:** Next.js — case review, HITL queue, network visualisation, ML admin  
✅ **Security:** JWT auth, 8 role types, full audit trail on every decision  
✅ **Scalability:** Celery + Redis async processing, horizontal scaling ready  

The only thing missing is production data and your authorisation to connect to InsureMaster.

---

## SLIDE 9 — WHAT I'M ASKING FOR (12:00–13:30)

### Three Approvals. One Decision.

1. **Budget: KES 11.5M (Year 1)**
   — Integration sprint, cloud infrastructure, compliance review

2. **IT Window: Q4 2026**
   — 90-day integration with InsureMaster; no disruption to existing systems

3. **Compliance Sign-off**
   — IRA data governance review; we will support this process with full documentation

---

## SLIDE 10 — CLOSE (13:30–15:00)

### The Ask Is Simple

> *KES 11.5 million investment.*  
> *KES 148 million return in Year 1.*  
> *Payback in 28 days.*  
> *The technology works. The ROI is proven. The risk is managed.*

**Go. Deploy ClaimGuard.**

Questions?

---

*Shantelle Wambui Kungu | shantellewambuikungu@gmail.com | github.com/Shantelle-wambui*
