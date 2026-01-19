# Fiscal Patriots - Optimized Main Branch Layout

## Target Repository Structure

```
fiscal-patriots/
│
├── README.md                           # Comprehensive project README
├── LICENSE                             # MIT License
├── .gitignore
│
├── deliverables/                       # 🎯 JUDGE-FACING
│   ├── README.md
│   ├── dashboard/
│   │   ├── README.md
│   │   ├── AGA_Datathon_USAspending.twbx
│   │   └── FAC_Merged_AGA_Datathon.twbx
│   ├── model/
│   │   ├── README.md
│   │   ├── Datathon_Predictive_Modeling_v3.ipynb
│   │   └── features.md
│   ├── report/
│   │   ├── README.md
│   │   └── Fiscal_Patriots_Report.pdf
│   ├── slides/
│   │   ├── README.md
│   │   └── Fiscal_Patriots_Presentation.pdf
│   └── video/
│       ├── README.md
│       └── [video file or link]
│
├── data/                               # 📊 ANALYSIS OUTPUTS
│   ├── README.md
│   ├── analysis_core/
│   │   ├── FAC_USAspending_Merged_Detail.csv
│   │   ├── FAC_USAspending_Merged_Detail_Data_Dictionary.docx
│   │   ├── FAC_USAspending_Summary_By_Tier.csv
│   │   ├── FAC_USAspending_Summary_By_Tier_Data_Dictionary.docx
│   │   ├── FAC_USAspending_Top_10_Red_By_Federal_Funding.csv
│   │   └── FAC_USAspending_Top_10_Red_By_Federal_Funding_Data_Dictionary.docx
│   ├── fac/
│   │   ├── FAC_Master_With_Risk_Score.csv
│   │   ├── FAC_Master_With_Risk_Score_Data_Dictionary.docx
│   │   └── FAC_Risk_Summary_By_Tier.csv
│   ├── sam/
│   │   ├── SAM_Exclusions_with_UEI.csv
│   │   └── SAM_Master_Data_Dictionary.docx
│   ├── merged/
│   │   ├── SAM_FAC_Merged.csv
│   │   ├── SAM_FAC_Merged_Data_Dictionary.docx
│   │   ├── SAM_USAspending_Merged.csv
│   │   └── SAM_USAspending_Merged_Data_Dictionary.docx
│   └── ml/
│       ├── FAC_ML_Train.csv
│       ├── FAC_ML_Test.csv
│       └── FAC_USAspending_ML_Training_Data_Dictionary.docx
│
├── pipeline/                           # 🔧 DATA PROCESSING
│   ├── README.md
│   ├── alteryx/
│   │   ├── FAC_Master_With_Risk_Score.yxmd
│   │   ├── FAC_USAspending_Merged.yxmd
│   │   ├── SAM_Exclusion_Cleaning.yxmd
│   │   ├── SAM_FAC_Merged.yxmd
│   │   └── SAM_USAspending_Merged.yxmd
│   ├── data_contract.md
│   └── inputs_outputs.md
│
├── docs/                               # 📚 DOCUMENTATION
│   ├── README.md
│   ├── appendix_hubs/
│   │   ├── case_studies/
│   │   │   ├── example_drilldown_one_red_entity.md
│   │   │   ├── full_audit_findings.md
│   │   │   ├── full_audit_findings_for_flagged_entities.md
│   │   │   ├── sam_exclusions_crosscheck_examples.md
│   │   │   └── supporting_documentation.md
│   │   ├── data_sources/
│   │   │   ├── allowable_data_sources_competition_rules.md
│   │   │   ├── data_dictionaries_in_repo.md
│   │   │   ├── fac_dataset_overview_and_files_used.md
│   │   │   ├── sam_exclusions_public_extract.md
│   │   │   └── usaspending_api_and_dictionary.md
│   │   ├── methodology/
│   │   │   ├── alteryx_workflows_and_screenshots.md
│   │   │   ├── data_acquisition_notes.md
│   │   │   ├── join_logic_uei_mapping.md
│   │   │   ├── outputs_and_reproducibility.md
│   │   │   └── pipeline_overview_visual.md
│   │   ├── ml/
│   │   │   ├── feature_list_and_importance.md
│   │   │   ├── final_ml_ready_outputs.md
│   │   │   ├── ml_training_dataset_build_workflow.md
│   │   │   ├── model_validation_metrics.md
│   │   │   └── train_test_split_methodology.md
│   │   ├── regulatory/
│   │   │   ├── 2cfr200_subpart_f.md
│   │   │   ├── gao_05_479.md
│   │   │   ├── gao_09_174.md
│   │   │   └── other_standards.md
│   │   └── scoring/
│   │       ├── final_scoring_outputs.md
│   │       ├── problem_entity_rule.md
│   │       ├── score_formula_and_tiers.md
│   │       ├── variable_definitions.md
│   │       └── weighting_rationale.md
│   ├── competition/
│   │   ├── AGA_2026_Datathon_Kick-Off_Call.pptx
│   │   ├── Allowable_Data_Sources.png
│   │   └── Prior_Winners_Video_Presentations.docx
│   ├── presentation/
│   │   ├── Fiscal_Patriots_Presentation_Guide.docx
│   │   ├── Presentation_Outline.docx
│   │   └── Project_Ideas_and_Societal_Impact.docx
│   └── team/
│       ├── Fiscal_Patriots_Team_Hub.docx
│       └── Meeting_Notes.docx
│
├── webapp/                             # 🌐 WEBSITE
│   ├── README.md
│   └── index.html                      # Latest production version
│
└── assets/                             # 🖼️ VISUALS
    ├── dashboard.png
    ├── pipeline.png
    └── logo.png
```

---

## Quick Migration Commands

```bash
# 1. Rename folders (remove spaces)
git mv "ML model" deliverables/model
git mv "webapp development" webapp
git mv "pipeline/alteryx workflow (main)" pipeline/alteryx

# 2. Clean webapp versions (keep only latest)
cd webapp
git rm sample_webapp_aga_datathon_v[1-9].html
git rm sample_webapp_aga_datathon_v10.html
git mv sample_webapp_aga_datathon.html index.html  # or latest version

# 3. Remove temp files
git rm "deliverables/model/temp"

# 4. Add missing files from archive branch
git checkout archive/onedrive-snapshot -- "archive/onedrive/AGA_Datathon_OneDrive/Datasets/FAC/CSV Files/FAC_Master_With_Risk_Score.csv"
mv "archive/onedrive/..." data/fac/

# 5. Commit changes
git add -A
git commit -m "chore: restructure repo for submission"
```

---

## Folder Purposes

| Folder | Purpose | Audience |
|--------|---------|----------|
| `deliverables/` | Competition submissions (dashboard, slides, video, model, report) | Judges |
| `data/` | Analysis-ready datasets with data dictionaries | Technical reviewers |
| `pipeline/` | Alteryx workflows for reproducibility | Code reviewers |
| `docs/` | Deep documentation, methodology, regulatory references | Anyone wanting details |
| `webapp/` | Website source code | Developers |
| `assets/` | Images and visuals | README rendering |

---

## Files to Add from Archive

| File | Source Branch | Destination |
|------|---------------|-------------|
| `FAC_Master_With_Risk_Score.csv` | `archive/onedrive-snapshot` | `data/fac/` |
| `FAC_Master_With_Risk_Score.yxmd` | `archive/onedrive-snapshot` | `pipeline/alteryx/` |
| `SAM_Exclusions_with_UEI.csv` | `archive/onedrive-snapshot` | `data/sam/` |
| `SAM_Exclusion_Cleaning.yxmd` | `archive/onedrive-snapshot` | `pipeline/alteryx/` |
| `SAM_FAC_Merged.csv` | `archive/onedrive-snapshot` | `data/merged/` |
| `SAM_USAspending_Merged.csv` | `archive/onedrive-snapshot` | `data/merged/` |
| `FAC_ML_Train.csv` | `archive/onedrive-snapshot` | `data/ml/` |
| `FAC_ML_Test.csv` | `archive/onedrive-snapshot` | `data/ml/` |
| `Datathon Predictive Modeling v3.ipynb` | `origin` | `deliverables/model/` |

---

## Files to Remove/Clean

| File | Reason |
|------|--------|
| `ML model/temp` | Temporary file |
| `sample_webapp_aga_datathon_v1.html` through `v9.html` | Old versions |
| Any `.DS_Store` files | macOS artifacts |
| Any `__pycache__/` directories | Python cache |

---

## Naming Conventions

### Folders
- Use lowercase with underscores: `analysis_core/`, `data_sources/`
- No spaces or special characters
- Short but descriptive

### Files
- Use PascalCase for data files: `FAC_USAspending_Merged_Detail.csv`
- Use lowercase for markdown: `README.md`, `features.md`
- Use underscores not spaces: `Fiscal_Patriots_Presentation.pdf`
