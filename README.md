# Fiscal Patriots

## Team (Fiscal Patriots)

| Name | Role | Phone | Bio |
|------|------|------|------|
| Khaled Alkurd | Team Lead | GMU Spring '26 Accounting and Business Analytics, Alteryx, Tableau, R
| Pranavi Doodala | Project Manager | GMU Spring '26 Business Analytics; Data Mining, Predictive Modeling, Project Management
| Mariam Debas | Visualization Lead | GMU Spring '26 Accounting, Data Analytics, Tableau, R
| Nikita Chandrasing | Product Manager | GMU Fall '25 Business Analytics and MIS; Data Mining, Data Visualization, Product Design
| Andy Yaro | Product Developer | GMU Fall '28 Cybersecurity Engineering; python, git, aws

**AuditsMadeSimple • AGA Datathon 2026**

> A public-facing educational platform helping citizens understand federal financial assistance and audit data.

🌐 **Live Website:** https://gmufiscalpatriots.bytechisel.com

📊 **Presentation:** [View Presentation on Canva](https://www.canva.com/design/DAG-i1oWD9I/f_YqGEZFJ-amtJ2KuGCMFA/view?utm_content=DAG-i1oWD9I&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h2f1e7a7836)

▶️ **Video Walkthrough:** [Watch on YouTube](https://youtu.be/i0x2yidgPiY)

---

## Development Tools

| Category | Tools | Used For |
| --- | --- | --- |
| Data Processing | [Alteryx](https://www.alteryx.com/), [Python](https://www.python.org/) | Data cleaning, merging, Audit Health Score pipeline |
| Visualization | [Tableau Public](https://public.tableau.com/) | Interactive dashboards embedded on the platform |
| Machine Learning | [scikit-learn](https://scikit-learn.org/) | HistGradientBoosting classifier, permutation importance |
| Interpretability | [SHAP](https://shap.readthedocs.io/) | Feature-level impact analysis for model transparency |
| Website | HTML, CSS, [AWS](https://aws.amazon.com/) | Static site hosting and deployment |
| AI Assistance | [Claude](https://claude.ai/), [Google Gemini](https://gemini.google.com/) | Code generation assistance and iterative development |

---

## Python Libraries

| Library | Purpose |
| --- | --- |
| [`scikit-learn`](https://scikit-learn.org/) | Model training, evaluation (ROC-AUC), permutation importance |
| [`pandas`](https://pandas.pydata.org/) | Data cleaning, feature engineering, entity-year aggregation |
| [`numpy`](https://numpy.org/) | Numerical operations and array handling |
| [`shap`](https://shap.readthedocs.io/) | SHAP value analysis for model interpretability |
| [`matplotlib`](https://matplotlib.org/) | Feature importance and performance visualization |

---

## Key Findings

- **$8.58 trillion** in federal financial assistance distributed (FY2019–2024)
- **Top 10 states** received 50.9% of all federal grants
- **California alone** received $1.05 trillion (12% of total)
- **HHS and USDA** account for 67% of all federal assistance
- **57,448 entities** required to submit Single Audits (FY2016–2024)
- **16,300+ entities** had at least one audit finding

---

## Why This Exists

Federal funding data is large, fragmented, and hard to interpret quickly. Audit data is even harder because it uses specialized terminology and the impact is not always obvious. Our goal is to make these systems approachable for everyone.

**This project helps users:**
- Explore funding patterns by geography and time
- Learn audit terminology with plain-language definitions
- Follow guided examples (case studies and next steps) to investigate audit data more deeply

---

## Key Features of AuditsMadeSimple

### 1) Interactive Exploration (Tableau)
Dashboards that highlight:
- Funding distribution across states
- Funding trends over time
- Major funding sources by federal agency
- Higher-risk entities with funding context

### 2) Financial Literacy Glossary
A glossary translating common audit and spending terms into short, usable definitions.

### 3) Dataset Guide
Plain descriptions of USAspending, FAC, and SAM: what each tracks, what each misses, and how to use them responsibly.

### 4) Guided Engagement (Case Studies + What’s Next)
Short walkthroughs and a checklist-style “What’s next?” page that keeps visitors engaged after their first chart.

---

## Integrated Data Sources

We connect official public sources using **UEI (Unique Entity Identifier)** whenever possible.

| Source | What It Tracks |
|--------|-----------------|
| **USAspending.gov** | Federal spending and award transactions: who received funds, how much, and from which agency |
| **FAC.gov** | Single Audit submissions for non-federal entities expending $750K+ in federal awards |
| **SAM.gov** | Governmentwide exclusions: debarments, suspensions, and other exclusion actions |

---

## Repo Structure (Main Branch)
```
deliverables/   Submission artifacts (dashboards, slides, report, video)
webapp/         Website source (HTML pages + assets)
data/           Clean outputs (CSV + Hyper) organized by domain
pipeline/       Alteryx workflows + pipeline notes
docs/           Data dictionaries + appendix hubs + team/competition docs
models/         ML model notebooks, outputs, and screenshots
```

---

## Methodology Screenshots (Alteryx)

These live in:
`docs/appendix_hubs/methodology/screenshots/alteryx/`

**USAspending transformations**

USAspending transaction-level data was transformed into recipient-level summaries for each fiscal year (2019–2024), then combined for cumulative analysis. Outputs were exported to CSV and Tableau Hyper formats for dashboard integration.

![USAspending All Years](docs/appendix_hubs/methodology/screenshots/alteryx/USAspending_All_Years.png)
![USAspending FY2023](docs/appendix_hubs/methodology/screenshots/alteryx/USAspending_FY2023.png)
![USAspending FY2024](docs/appendix_hubs/methodology/screenshots/alteryx/USAspending_FY2024.png)

**FAC Master Clean**

Four FAC tables (General, Findings, Corrective Action Plans, Federal Awards) were joined and aggregated to entity level by `auditee_uei`, producing 57.4K clean audited entity records. Outputs preserve audit flags, finding counts, and federal expenditure amounts for risk scoring and USAspending integration.

![FAC Master Clean](docs/appendix_hubs/methodology/screenshots/alteryx/FAC%20Master%20Clean.png)

**Audit Health Score construction**

The Audit Health Score was calculated for each entity using weighted risk factors including going concern (25 pts), material weakness (20 pts), repeat findings (15 pts), and significant deficiencies (10 pts), with mitigating factors applied. Entities were tiered into Red, Yellow, and Green categories to support dashboard visualizations and funding analysis.

![FAC Master With Risk Score](docs/appendix_hubs/methodology/screenshots/alteryx/FAC_Master_With_Risk_Score.png)

**FAC + USAspending Merge**

FAC audit data was joined to USAspending financial assistance records on UEI to link audit findings with federal funding received. This merge enables analysis of how much taxpayer money flowed to entities with material weaknesses, repeat findings, or going concern flags.

![FAC USAspending Merged](docs/appendix_hubs/methodology/screenshots/alteryx/FAC_USAspending_Merged.png)

**SAM + FAC Merge**

SAM exclusion data was joined to FAC audit records on UEI to identify entities with both exclusion history and audit findings. This cross-reference supports transparency gap analysis of debarred or suspended entities.

![SAM FAC Merged](docs/appendix_hubs/methodology/screenshots/alteryx/SAM_FAC_Merged.png)

**SAM Exclusion Cleaning**

SAM exclusion records were split by UEI availability (38K with UEI, 120K legacy records without), with date parsing to calculate exclusion duration and active status. Outputs support transparency gap analysis and cross-referencing of excluded entities against federal award recipients.

![SAM Exclusion Cleaning](docs/appendix_hubs/methodology/screenshots/alteryx/SAM_Exclusion_Cleaning.png)

---

## Methodology Screenshots (Tableau)

These live in:
`docs/appendix_hubs/methodology/screenshots/tableau/`

**Funding Distribution & Trends**

These visualizations show where federal financial assistance flows geographically and how funding levels changed over the six-year period. The Top 10 states account for over half of all federal grants, with California alone receiving 12% of the national total.

![Bar - Top 10 States Receive 50.9% of All Federal Grants](docs/appendix_hubs/methodology/screenshots/tableau/Bar%20-%20Top%2010%20States%20Receive%2050.9%25%20of%20All%20Federal%20Grants.png)
![Cumulative Federal Funding (FY2019-2024)](docs/appendix_hubs/methodology/screenshots/tableau/Cumulative%20Federal%20Funding%20%28FY2019-2024%29.png)
![Federal Funding (FY2019-2024)](docs/appendix_hubs/methodology/screenshots/tableau/Federal%20Funding%20%28FY2019-2024%29.png)
![Federal Funding by Top 5 States (FY2019-2024)](docs/appendix_hubs/methodology/screenshots/tableau/Federal%20Funding%20by%20Top%205%20States%20%28FY2019-2024%29.png)

**Audit Oversight Signals**

These maps highlight where audit findings are concentrated relative to funding received. Material weakness rates vary significantly by state, revealing geographic patterns in internal control quality.

![Findings Per $1M in Federal Spending by State](docs/appendix_hubs/methodology/screenshots/tableau/Findings%20Per%20%241M%20in%20Federal%20Spending%20by%20State.png)
![Map - Material Weakness by State](docs/appendix_hubs/methodology/screenshots/tableau/Map%20-%20Material%20Weakness%20by%20State.png)
![Map - Material Weakness Rate by State](docs/appendix_hubs/methodology/screenshots/tableau/Map%20-%20Material%20Weakness%20Rate%20by%20State.png)

**Risk Tiering**

This visualization shows the relationship between Audit Health Score and federal funding received. Red-tier entities received disproportionately more funding than Green-tier entities with cleaner audit records.

![Risk vs Protection Red Tier Shows Worst Combination](docs/appendix_hubs/methodology/screenshots/tableau/Risk%20vs%20Protection%20Red%20Tier%20Shows%20Worst%20Combination.png)

---
## ML Model & Predictive Findings

We built a predictive model that acts as an early warning signal. It flags organizations that are more likely to have audit findings next year (t+1), using what we already know this year (t). The goal is to help oversight teams prioritize review and support when resources are limited.  
Full case study: https://gmufiscalpatriots.bytechisel.com/ml_model_casestudy.html

### Data and setup
- Data source: Federal Audit Clearinghouse (FAC), audit year files from 2019 to 2022.  
- Grain: one row per entity per audit year (entity-year panel). 110,739 total observations across 56,333 unique entities.  
- Entity key: Employer Identification Number (EIN), since Unique Entity Identifier (UEI) has many placeholders in earlier years.  
- Label: whether the entity has any findings in the next year (t+1), created by shifting outcomes forward within each entity.  
- Train/test split: time-based. Trained on 2019–2020, tested on 2021 to prevent data leakage.
  
### Model and performance
- Model: Histogram-based Gradient Boosting (HistGradientBoostingClassifier), from scikit-learn.  
- Primary metric: ROC-AUC = 0.7656 — the model correctly ranks a risky entity above a non-risky one 77% of the time.  
- Secondary metric: PR-AUC = 0.5439 (3x the random baseline of 0.18), reflecting strong positive-class concentration despite class imbalance in audit findings.
  
### What the model learned
We used permutation feature importance and SHAP (SHapley Additive Explanations) to keep results explainable. Top signals included:
- prior findings indicators (whether findings happened, and how many)
- total federal expenditures
- breadth across agencies (distinct agencies)
- award structure (direct award lines)

SHAP analysis confirmed that prior findings are the dominant predictor, with high feature values pushing predictions strongly toward positive (finding expected). This directional insight informed the weighting used in the Audit Health Score.

### Figures
![Figure 1: Feature importance](<models/predictive_audit_findings/screenshots/figure_2_roc_auc_feature_importance.png>)
![Figure 2: Model performance](<models/predictive_audit_findings/screenshots/figure 1.png>)
![Figure 3: SHAP beeswarm](<models/predictive_audit_findings/screenshots/figure 2.png>)

## How to Explore the Project

1. Visit the live site: https://gmufiscalpatriots.bytechisel.com  
2. Open the Tableau dashboards (linked from the site)
3. Read the glossary to understand audit terminology
4. Use “What’s next?” to follow guided questions and case studies

---

## Disclaimer

This project is for educational and public understanding purposes. Audit and exclusion signals require context. The presence of a finding or a higher-risk tier is not proof of wrongdoing. Always validate conclusions using primary documentation, program context, and appropriate investigative standards.

---

<p align="center">
<b>Fiscal Patriots</b> • AuditsMadeSimple • AGA Datathon 2026<br>
George Mason University • Costello College of Business
</p>
