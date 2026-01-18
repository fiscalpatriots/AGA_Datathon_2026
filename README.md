# FISCAL PATRIOTS  
## AGA Datathon 2026

An interactive platform promoting financial literacy by making federal spending and audit data accessible to everyday citizens.

**Explore the Dashboard →** https://gmufiscalpatriots.bytechisel.com
---

## The Problem

Federal accountability data is fragmented across multiple systems. Exclusion data doesn't flow between agencies, and citizens lack the tools to understand how their tax dollars are spent.

---

## Our Solution

Fiscal Patriots integrates three federal data sources into a single, accessible platform:

| Source | What It Contains | Records |
|---|---|---|
| USAspending.gov | Federal financial assistance | 74M (FY2019-2024) |
| FAC.gov | Single audit findings & compliance | 57K entities |
| SAM.gov | Excluded & debarred entities | 167K records |

**Total federal assistance analyzed:** **$8.58 trillion**

---

## Key Findings

Cross-system analysis revealed oversight gaps not visible in any single dataset:

| Data Merge | Entity | Finding |
|---|---|---|
| FAC + SAM | Prince Hall Village Charitable Trust | Excluded by HUD in 1997, still receiving HUD funds in 2022. Gap: 25+ years |
| SAM + USAspending | Amerihost Services, LLC | Excluded by EPA in 2021, received $759K across 15 HUD awards through 2024. Gap: 3+ years |

➡️ **Recommendation:** Automated pre-payment exclusion verification

---

## Features

| Feature | Description |
|---|---|
| Exploratory Visualizations | Interactive Tableau dashboards showing funding flows by state, time, and program |
| Financial Literacy Glossary | Searchable audit terminology for non-technical users |
| Audit Health Score | 0-100 risk metric (Green/Yellow/Red tiers) for entity oversight prioritization |
| Case Studies | Real examples demonstrating cross-system data integration value |

---

## Audit Health Score

A screening metric that summarizes audit oversight signals into interpretable tiers:

| Tier | Score | Interpretation |
|---|---:|---|
| Green | 80-100 | Fewer oversight signals - continue standard validation |
| Yellow | 60-79 | Moderate signals - review patterns, check year-over-year |
| Red | 0-59 | Highest signals - prioritize for deeper review |

**Note:** Red tier ≠ fraud. It means "more audit flags warrant review."

---

## Tools & Technologies

| Category | Tools |
|---|---|
| Data Processing | Alteryx, Python |
| Visualization | Tableau Public |
| Machine Learning | HistGradientBoosting (scikit-learn) |
| Website | HTML, CSS, AWS |

---

## Team

| Name | Role |
|---|---|
| Khaled Alkurd | Team Lead |
| Pranavi Doodala | Project Manager |
| Mariam Debas | Visualization Lead |
| Nikita Chandrasing | Product Manager |
| Andy Yaro | Product Developer |

---

## Deliverables

| Deliverable | Location |
|---|---|
| Dashboard | [Live Site URL] |
| Tableau Workbooks | deliverables/dashboard/ |
| Slides (PDF) | deliverables/slides/Fiscal Patriots Presentation.pdf |
| Video | deliverables/video/README.md |
| Report | deliverables/report/README.md |

---

## Repository Structure

```text
├── deliverables/          # Dashboard, slides, video, report
├── data/analysis_core/    # Merged datasets & dictionaries
├── pipeline/alteryx/      # Data cleaning workflows
├── docs/                 # Competi

# Fiscal Patriots | AuditsMadeSimple (AGA Datathon 2026)

**AuditsMadeSimple** is a public-facing, educational platform that helps people explore **federal financial assistance** (grants and related awards) alongside **audit oversight signals**. We connect spending data with audit context so users can understand where funding goes, what audit terms mean, and how to responsibly prioritize follow-up questions.

Live website: https://gmufiscalpatriots.bytechisel.com

---

## Why this exists

Federal funding data is large, fragmented, and hard to interpret quickly. Audit data is even harder because it uses specialized terminology and the impact is not always obvious. Our goal is to make these systems approachable without oversimplifying the responsibility required to interpret oversight data.

This project helps a user:
- Explore funding patterns by geography and time
- Learn audit terminology with plain-language definitions
- Use a screening signal (Audit Health Score) to identify entities that may merit a closer look
- Follow guided examples (case studies and next steps) to investigate responsibly

---

## What we built

### 1) Interactive exploration (Tableau)
Dashboards that highlight:
- Funding distribution across states
- Funding trends over time
- Major funding sources by federal agency
- High-risk entities with funding context

### 2) Audit glossary (plain language)
A glossary section to translate common audit and spending terms into short, useful explanations.

### 3) Guided engagement (case studies and “What’s next?”)
Short walkthroughs and a checklist-style next step page that keeps visitors engaged and shows what to do after the first chart.

### 4) Audit Health Score (screening signal)
A simple, interpretable score designed to help users prioritize where to look deeper without claiming wrongdoing.

---

## Data sources we connect

We work from official public sources and join data using **UEI (Unique Entity Identifier)** whenever possible:

- **USAspending.gov**: federal spending and award transactions.
- **FAC.gov (Federal Audit Clearinghouse)**: single audit submissions for non-federal entities that expend large amounts of federal awards.
- **SAM.gov (System for Award Management) Exclusions**: governmentwide exclusions (for example, debarments and suspensions) where available.

---

## Key datasets and deliverables in this repo

These are the primary analysis outputs used by the dashboards and website content.

### FAC + USAspending merged detail (entity-level)
Merged dataset that combines FAC audit indicators with USAspending funding context.

- File: `FAC_USAspending_Merged_Detail.csv`
- Data dictionary: `FAC_USAspending_Merged_Detail_Data_Dictionary.docx`

### Summary by Audit Health Score tier
Aggregated rollups by tier (Green, Yellow, Red) to show how funding and entity counts distribute across tiers.

- File: `FAC_USAspending_Summary_By_Tier.csv`
- Data dictionary: `FAC_USAspending_Summary_By_Tier_Data_Dictionary.docx`

### Top 10 Red tier entities by federal funding
A shortlist used for drilldowns, examples, and case studies.

- Data dictionary: `FAC_USAspending_Top_10_Red_By_Federal_Funding_Data_Dictionary.docx`
- (If present in the branch) corresponding Top 10 CSV output.

### Audit Health Score master output
A consolidated dataset including computed risk points and the Audit Health Score.

- File: `FAC_Master_With_Risk_Score.csv`
- Workflow: `FAC_Master_With_Risk_Score.yxmd` (Alteryx workflow)

### Tableau workbooks (dashboards)
Packaged Tableau workbooks used to publish and iterate on visuals.

- `AGA datathon visualizations - USAspending Updated.twbx`
- `FAC-Merged set AGA datathon.twbx`
- `Book1.twbx`
- `Book3.twbx`

### Website artifacts (front-end)
The website is hosted separately, but the repo includes working HTML builds used during development.

- `sample_webapp_aga_datathon_v17.html`
- `sample_webapp_aga_datathon_v18.html`

---

## Audit Health Score

The **Audit Health Score** is a 0 to 100 screening signal intended for interpretability.

**Definition**
- Audit Health Score = 100 − Risk Points
- Risk Points are capped to keep the score in a stable 0 to 100 range.

**Tiering**
- Green: 80 to 100 (lower risk)
- Yellow: 60 to 79 (moderate risk)
- Red: 0 to 59 (higher risk)

**Example risk signals**
Risk Points can increase based on factors such as:
- severity of findings and internal control issues
- repeat findings across years
- questioned costs indicators
- audit opinion or going concern style indicators (when present)

Risk Points can be reduced by factors such as:
- low-risk auditee style indicators (when present)
- stronger corrective action patterns (when measurable)

Important: this score is a prioritization aid, not a verdict. It does not prove fraud, waste, or abuse. It is meant to help focus questions and guide responsible follow-up.

---

## Predictive modeling prototype (early warning)

We include an early prototype to explore whether audit and funding history can help anticipate future risk signals.

- Goal: entity-year prediction (use year t to predict findings signals in year t + 1)
- Approach: gradient boosting style classification on engineered features
- Feature families (examples): prior findings counts and flags, award volume, funding totals, funding mix, and agency or program diversity

This is a prototype for learning and prioritization, not an operational system.

---

## How to reproduce (high level)

1. Collect raw extracts from USAspending, FAC, and exclusions (when needed).
2. Standardize identifiers, especially UEI formatting and missingness handling.
3. Compute risk indicators and Risk Points.
4. Convert Risk Points into the Audit Health Score and tier labels.
5. Merge FAC audit context with USAspending funding context on UEI.
6. Export analysis outputs used by Tableau and the website.

If you are using the existing workflow artifacts, start with:
- `FAC_Master_With_Risk_Score.yxmd` (builds Audit Health Score fields)
- `FAC_USAspending_Merged_Detail.csv` (merged analysis output)

---

## How to explore the project quickly

If you want the fastest tour:

1. Visit the live site: https://gmufiscalpatriots.bytechisel.com  
2. Open the Tableau dashboards (published links are accessible from the site).
3. Read the glossary section to understand the terms used in audit reporting.
4. Use the “What’s next?” page to follow guided questions.

---

## Team (Fiscal Patriots)

- Khaled Alkurd (Team Lead)
- Pranavi Doodala (Project Manager)
- Mariam Debas (Visualization Lead)
- Nikita Chandrasing (Product Manager)
- Andy Yaro (Product Developer)

---

## Disclaimer

This project is for educational and public understanding purposes. Audit and exclusion signals require context. The presence of a finding or a higher-risk tier is not proof of wrongdoing. Always validate conclusions with primary documentation, program context, and proper investigative standards.
