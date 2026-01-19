# Fiscal Patriots

**AuditsMadeSimple  •  AGA Datathon 2026**

> A public-facing educational platform helping citizens explore federal financial assistance alongside audit oversight signals

🌐 **Live Website:** [gmufiscalpatriots.bytechisel.com](https://gmufiscalpatriots.bytechisel.com)

---

## Why This Exists

Federal funding data is large, fragmented, and hard to interpret quickly. Audit data is even harder because it uses specialized terminology and the impact is not always obvious. Our goal is to make these systems approachable without oversimplifying the responsibility required to interpret oversight data.

**This project helps users:**
- Explore funding patterns by geography and time
- Learn audit terminology with plain-language definitions
- Use a screening signal (Audit Health Score) to identify entities that may merit a closer look
- Follow guided examples (case studies and next steps) to investigate responsibly

---

## What We Built

### 1. Interactive Exploration (Tableau)
Dashboards that highlight:
- Funding distribution across states
- Funding trends over time
- Major funding sources by federal agency
- High-risk entities with funding context

### 2. Financial Literacy Glossary
A glossary section translating common audit and spending terms into short, useful explanations — making government accountability language accessible for everyday citizens.

### 3. Dataset Guide
Descriptions of USAspending, FAC, and SAM — what each tracks, what it misses, and how to navigate them for your own research questions.

### 4. Guided Engagement (Case Studies & What's Next)
Short walkthroughs and a checklist-style next steps page that keeps visitors engaged and shows what to do after the first chart.

### 5. Audit Health Score (Screening Signal)
A simple, interpretable 0-100 score designed to help users prioritize where to look deeper — without claiming wrongdoing.

---

## Integrated Data Sources

We connect official public sources using UEI (Unique Entity Identifier) whenever possible:

| Source | What It Tracks | Coverage |
|--------|----------------|----------|
| **USAspending.gov** | Federal spending and award transactions — who received funds, how much, from which agency | 74M records |
| **FAC.gov** | Single Audit submissions for non-federal entities expending $750K+ in federal awards | 57K entities |
| **SAM.gov** | Governmentwide exclusions — debarments, suspensions, and other exclusion actions | 167K records |

---

## Key Findings from Data Integration

Cross-system analysis revealed oversight gaps invisible in any single dataset:

### FAC + SAM Merge
**Prince Hall Village Charitable Trust** — Excluded by HUD in 1997, still receiving HUD funds in 2022.

🔴 **Gap: 25+ years** • Intra-agency failure: the same agency that excluded them continued funding them.

### SAM + USAspending Merge
**Amerihost Services, LLC** — Excluded by EPA in 2021, received $759K across 15 HUD awards through 2024.

🔴 **Gap: 3+ years** • Cross-agency failure: exclusion data doesn't flow between agencies.

> ✅ **Recommendation: Automated pre-payment exclusion verification**

---

## Audit Health Score

A 0-100 screening signal designed for interpretability and responsible prioritization.

### Definition
```
Audit Health Score = 100 − Risk Points (capped to keep score in 0-100 range)
```

### Tiering

| Tier | Score | Interpretation |
|------|-------|----------------|
| 🟢 **Green** | 80-100 | Fewer oversight signals — continue standard validation |
| 🟡 **Yellow** | 60-79 | Moderate signals — review patterns year-over-year |
| 🔴 **Red** | 0-59 | Highest oversight signals — prioritize for deeper review |

### Risk Signals (Examples)

**Risk Points increase based on:**
- Severity of findings and internal control issues
- Repeat findings across years
- Questioned costs indicators
- Going concern or modified opinion indicators

**Risk Points decrease based on:**
- Low-risk auditee designation
- Stronger corrective action patterns

> ⚠️ **Important:** This score is a prioritization aid, not a verdict. It does not prove fraud, waste, or abuse.

---

## Predictive Modeling Prototype

An early prototype exploring whether audit and funding history can help anticipate future risk signals.

- **Goal:** Entity-year prediction (use year t to predict findings in year t+1)
- **Approach:** HistGradientBoosting classification on engineered features
- **Feature families:** Prior findings counts/flags, award volume, funding totals/mix, agency/program diversity
- **Performance:** ROC-AUC 0.7656, PR-AUC 0.5439

*This is a prototype for learning and prioritization, not an operational system.*

---

## Key Datasets & Deliverables

| Dataset | File / Path |
|---------|-------------|
| FAC + USAspending Merged Detail | `FAC_USAspending_Merged_Detail.csv` |
| Summary by Tier | `FAC_USAspending_Summary_By_Tier.csv` |
| Top 10 Red by Federal Funding | `FAC_USAspending_Top_10_Red_By_Federal_Funding.csv` |
| Audit Health Score Master | `FAC_Master_With_Risk_Score.csv` |
| Alteryx Workflow (Risk Score) | `FAC_Master_With_Risk_Score.yxmd` |

*Each dataset includes a corresponding data dictionary (.docx).*

### Tableau Workbooks
- `AGA datathon visualizations - USAspending Updated.twbx`
- `FAC-Merged set AGA datathon.twbx`

---

## Repository Structure

```
├── deliverables/
│   ├── dashboard/      # Tableau workbooks
│   ├── slides/         # Presentation PDF
│   ├── video/          # Video submission
│   └── report/         # Written report
├── data/
│   └── analysis_core/  # Merged datasets & dictionaries
├── pipeline/
│   └── alteryx/        # Workflow files (.yxmd)
├── docs/               # Competition & team docs
└── assets/             # Visuals and images
```

---

## How to Explore the Project

For the fastest tour:

1. **Visit the live site:** [gmufiscalpatriots.bytechisel.com](https://gmufiscalpatriots.bytechisel.com)
2. **Open the Tableau dashboards** (links accessible from the site)
3. **Read the glossary section** to understand audit terminology
4. **Use the "What's Next?" page** to follow guided questions

---

## How to Reproduce (High Level)

1. Collect raw extracts from USAspending, FAC, and SAM exclusions
2. Standardize identifiers (UEI formatting, missingness handling)
3. Compute risk indicators and Risk Points
4. Convert Risk Points into Audit Health Score and tier labels
5. Merge FAC audit context with USAspending funding context on UEI
6. Export analysis outputs for Tableau and website

**Start with:** `FAC_Master_With_Risk_Score.yxmd` (Alteryx) → `FAC_USAspending_Merged_Detail.csv`

---

## Tools & Technologies

| Category | Tools |
|----------|-------|
| Data Processing | Alteryx, Python |
| Visualization | Tableau Public |
| Machine Learning | HistGradientBoosting (scikit-learn) |
| Website | HTML, CSS, AWS |

---

## Team (Fiscal Patriots)

| Name | Role |
|------|------|
| Khaled Alkurd | Team Lead |
| Pranavi Doodala | Project Manager |
| Mariam Debas | Visualization Lead |
| Nikita Chandrasing | Product Manager |
| Andy Yaro | Product Developer |

---

## Disclaimer

*This project is for educational and public understanding purposes. Audit and exclusion signals require context. The presence of a finding or a higher-risk tier is not proof of wrongdoing. Always validate conclusions with primary documentation, program context, and proper investigative standards.*

---

<p align="center">
<b>Fiscal Patriots</b> • AuditsMadeSimple • AGA Datathon 2026<br>
George Mason University • Costello College of Business
</p>
