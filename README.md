# AGA_Datathon_2026. Data Cleaning Branch

**AGA Datathon 2026 | Fiscal Patriots**

This branch contains data processing workflows and cleaned datasets for the Fiscal Patriot Dashboard.

---

## Folder Structure
```
Federal Audit ClearingHouse/   FAC Alteryx workflows + cleaned CSVs
USAspending/                   USAspending Alteryx workflows + cleaned CSVs
SAM/                           SAM exclusion workflows + cleaned CSVs
```

---

## Workflows

| Workflow | Description |
|----------|-------------|
| **USAspending_All_Years.yxmd** | Transforms transaction-level data into recipient-level summaries (FY2019–2024) |
| **USAspending_FY20XX.yxmd** | Yearly recipient-level summaries with fiscal year tagging |
| **FAC_Master_Clean.yxmd** | Joins 4 FAC tables, aggregates to entity level by `auditee_uei` (57.4K entities) |
| **FAC_Master_With_Risk_Score.yxmd** | Applies Audit Health Score weighting and risk tiering |
| **FAC_USAspending_Merged.yxmd** | Joins FAC audit data to USAspending awards on UEI |
| **SAM_Exclusion_Cleaning.yxmd** | Splits SAM exclusions by UEI, parses dates, calculates duration and active status |

---

## Data Sources

| Source | Files | Period |
|--------|-------|--------|
| USAspending.gov | Financial assistance awards | FY2019–2024 |
| FAC.gov | General, Findings, CAP, Federal Awards | FY2016–2024 |
| SAM.gov | Exclusion records | Through Dec 2025 |

---

## Outputs

All cleaned outputs exported as:
- `.csv` for analysis
- `.hyper` for Tableau integration
