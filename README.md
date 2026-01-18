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
