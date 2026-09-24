# Week11_Business_Case_ShantelWambui
## ClaimGuard: AI-Powered Insurance Fraud Detection
### Executive Business Case — For CFO / Board Approval

**Prepared by:** Shantelle Wambui Kungu | Data Analyst & AI/ML Engineer
**Date:** September 2026
**Classification:** Confidential — Board Use Only

---

## 1. Problem Statement

Kenya's motor insurance sector loses an estimated **KES 40–60 billion annually** to fraudulent claims (IRA Kenya, 2024). The current manual review process takes **5–15 days per claim**, employs a full team of adjusters, and still misses approximately **60% of fraud**. Each missed fraudulent claim costs an average of **KES 150,000**. For a mid-size insurer processing 2,000 claims per month, this translates to roughly **KES 14.4 million in undetected fraud losses every month** — a direct and avoidable hit to the combined ratio.

The core failure is structural: human reviewers cannot simultaneously cross-reference hundreds of claims. A single garage filing nine fraudulent claims across different policyholders over 90 days is completely invisible to an adjuster reading one file at a time.

---

## 2. Proposed Solution

**ClaimGuard** is a production-ready AI claims intelligence platform. It integrates with existing claims management systems via API and processes every claim through three detection layers:

| Layer | What It Does |
|---|---|
| **Rules Engine** | 8 motor fraud rules (claim within 14 days of inception, duplicate OB numbers, provider billing spikes, round-sum amounts, missing documents) |
| **ML Scorer** | XGBoost model with 25 engineered features produces a 0–1 fraud probability score |
| **Network Detector** | Graph analysis across providers, claimants, and vehicles — detects organised fraud rings invisible to individual reviewers |

Each claim is automatically routed: low-risk claims are approved, high-risk claims with rule violations are rejected, and medium-risk claims are escalated to a human adjuster with a **plain-English SHAP explanation** showing exactly why. Every decision is fully auditable for IRA compliance.

**Processing time: < 30 seconds per claim** (vs. 5–15 days manually).

---

## 3. Financial Impact

### Assumptions (mid-size insurer)
- Monthly claim volume: **2,000 claims**
- Fraud prevalence: **8%** = 160 fraudulent claims/month
- Current detection rate: **40%** (manual) → ClaimGuard: **81% recall**
- Average fraudulent claim value: **KES 150,000**

### Monthly & Annual Savings

| Savings Source | Calculation | Monthly | Annual |
|---|---|---|---|
| Additional fraud caught | (81%−40%) × 160 × KES 150K | KES 9.84M | KES 118.1M |
| Adjuster time savings | 95% reduction × 8 staff × KES 120K/month | KES 0.91M | KES 10.9M |
| False positive reduction | 40% fewer wrongly delayed claims × KES 5K rework cost | KES 1.60M | KES 19.2M |
| **Total** | | **KES 12.35M** | **KES 148.2M** |

### Investment

| Cost Item | Year 1 | Year 2+ |
|---|---|---|
| Development & integration | KES 8.5M | — |
| Cloud infrastructure | KES 1.8M | KES 1.8M |
| Maintenance & retraining | KES 1.2M | KES 1.2M |
| **Total** | **KES 11.5M** | **KES 3.0M** |

### ROI

```
Year 1 Net Benefit   =  KES 148.2M − KES 11.5M  =  KES 136.7M
Year 1 ROI           =  KES 136.7M ÷ KES 11.5M  =  1,188%
Payback Period       =  KES 11.5M ÷ KES 12.35M/month  =  0.93 months (~28 days)
5-Year NPV (10% DR)  =  KES 580M
```

**The system pays for itself within one month of deployment.**

---

## 4. Risks & Mitigation

| # | Risk | Mitigation |
|---|---|---|
| **1** | **Regulatory challenge** — IRA or a policyholder disputes an automated rejection | Every rejection includes a full SHAP explanation and mandatory human review step. No claim is auto-rejected without an auditable reason code. Designed to comply with IRA data governance guidelines. |
| **2** | **Model drift** — fraud patterns evolve faster than the model retrains | Automated monthly retraining pipeline with a champion/challenger model registry. Performance alert triggers if AUC-ROC drops below 0.78, prompting immediate review. |

---

## 5. Recommendation — GO ✅

**Approve full deployment of ClaimGuard.**

The investment is KES 11.5M. The Year 1 return is KES 148.2M. The payback period is 28 days. The technology is production-ready — backend built, containerised, and tested. What is required is a 90-day integration sprint with InsureMaster and IRA compliance sign-off.

**Approvals requested:**
1. **Budget:** KES 11.5M (Year 1)
2. **IT integration window:** Q4 2026 (90-day sprint)
3. **Compliance review:** IRA data governance sign-off

> *Every month we delay costs the business approximately KES 12 million in avoidable fraud losses.*
