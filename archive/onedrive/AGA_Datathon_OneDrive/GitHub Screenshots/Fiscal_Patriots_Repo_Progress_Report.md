# Fiscal Patriots GitHub Repository
## Restructuring Progress Report & Optimized Main Branch Layout

---

# PART 1: CURRENT STATE ANALYSIS

## Branch Overview (10 branches total)

| Branch | Files | Purpose | Status |
|--------|-------|---------|--------|
| `main` | 73 | Production branch | 🟡 Needs optimization |
| `origin` | 78 | Remote tracking | Mirrors main + 5 extra files |
| `archive/onedrive-snapshot` | 138 | Full OneDrive backup | ✅ Complete archive |
| `chore/repo-scaffold` | 55 | Professional scaffold template | 🔴 Not merged |
| `feature/data-cleaning` | 20 | USAspending & FAC cleaning workflows | 🔴 Not merged |
| `feature/data-intake` | 4 | ML training data prep | 🔴 Not merged |
| `feature/data-merge` | 4 | FAC + USAspending merge | 🔴 Not merged |
| `feature/dashboard` | 1 | Dashboard work | 🔴 Empty (README only) |
| `feature/modeling-forecast` | 1 | ML modeling | 🔴 Empty (README only) |
| `docs/report-and-slides` | 1 | Documentation | 🔴 Empty (README only) |

---

## Current Main Branch Structure (73 files)

```
main/
├── assets/                          ✅ Good
│   ├── dashboard.png
│   └── pipeline.png
├── data/                            ✅ Good structure
│   ├── analysis_core/
│   │   ├── merged_detail/           ✅ Has CSV + Data Dictionary
│   │   ├── summary_by_tier/         ✅ Has CSV + Data Dictionary
│   │   └── top_10_red_by_federal_funding/  ✅ Has CSV + Data Dictionary
│   └── README.md
├── deliverables/                    ✅ Good structure
│   ├── dashboard/                   ✅ Has 2 Tableau workbooks + README
│   ├── model/                       ⚠️ Only has features.md
│   ├── report/                      ⚠️ Only README placeholder
│   ├── slides/                      ✅ Has PDF
│   └── video/                       ⚠️ Only README placeholder
├── docs/                            ✅ Comprehensive
│   ├── appendix_hubs/               ✅ 24 documentation files
│   │   ├── case_studies/            (5 files)
│   │   ├── data_sources/            (5 files)
│   │   ├── methodology/             (5 files)
│   │   ├── ml/                      (5 files)
│   │   ├── regulatory/              (4 files)
│   │   └── scoring/                 (5 files)
│   ├── competition/                 ✅ Competition materials
│   ├── data_dictionaries/           ⚠️ Only USAspending dictionary
│   ├── presentation/                ✅ Presentation guides
│   └── team/                        ✅ Team hub + meeting notes
├── ML model/                        🔴 BAD: Space in folder name
│   ├── Datathon Predictive Modeling.ipynb
│   └── temp                         🔴 Should be removed
├── pipeline/                        ⚠️ Partially complete
│   ├── alteryx workflow (main)/     🔴 BAD: Space + parens in name
│   │   └── FAC_USAspending_Merged.yxmd
│   ├── data_contract.md
│   ├── inputs_outputs.md
│   └── README.md
├── webapp development/              🔴 BAD: Space in folder name
│   ├── README.md
│   └── sample_webapp_*.html         (11 version files - too many)
├── .gitignore
└── README.md
```

---

## Critical Issues Identified

### 🔴 HIGH PRIORITY

| Issue | Location | Impact |
|-------|----------|--------|
| Spaces in folder names | `ML model/`, `webapp development/`, `alteryx workflow (main)/` | Breaks scripts, bad practice |
| Missing Audit Health Score master | Not in main | Core deliverable missing |
| Missing FAC risk score workflow | `FAC_Master_With_Risk_Score.yxmd` | Reproducibility gap |
| Missing SAM exclusion data | No SAM outputs in main | Key findings data missing |
| Too many webapp versions | 11 HTML files | Clutter, only need latest |
| `temp` files present | `ML model/temp` | Should be gitignored |
| ML notebooks not in deliverables | In separate folder | Should be consolidated |

### 🟡 MEDIUM PRIORITY

| Issue | Location | Impact |
|-------|----------|--------|
| Missing video deliverable | `deliverables/video/` empty | Competition requirement |
| Missing report deliverable | `deliverables/report/` empty | Competition requirement |
| Data dictionaries scattered | Multiple locations | Hard to find |
| No LICENSE file | Root | Open source best practice |
| Feature branches not merged | 4 branches with work | Lost work |

### 🟢 LOW PRIORITY

| Issue | Location | Impact |
|-------|----------|--------|
| No CONTRIBUTING.md | Root | Community contribution |
| No .github/ folder | Root | PR templates, CI/CD |
| Scaffold branch unused | `chore/repo-scaffold` | Professional structure available |

---

## What's in Archive but Missing from Main

### Critical Files to Migrate

| File | Archive Location | Should Go To |
|------|------------------|--------------|
| `FAC_Master_With_Risk_Score.csv` | `archive/.../FAC/CSV Files/` | `data/fac/` |
| `FAC_Master_With_Risk_Score.yxmd` | `archive/.../FAC/Alteryx Workflows/` | `pipeline/alteryx/` |
| `SAM_Exclusions_with_UEI.csv` | `archive/.../SAM/CSV Files/` | `data/sam/` |
| `SAM_Exclusion_Cleaning.yxmd` | `archive/.../SAM/Alteryx Workflows/` | `pipeline/alteryx/` |
| `SAM_FAC_Merged.csv` | `archive/.../Merged/CSV Files/` | `data/merged/` |
| `SAM_USAspending_Merged.csv` | `archive/.../Merged/CSV Files/` | `data/merged/` |
| `FAC_ML_Train.csv` | `archive/.../ML Training/CSV Files/` | `data/ml/` |
| `FAC_ML_Test.csv` | `archive/.../ML Training/CSV Files/` | `data/ml/` |
| `Datathon Predictive Modeling v3.ipynb` | `origin/ML model/` | `deliverables/model/` |

---

## Branch Merge Strategy

### Recommended Actions

1. **Merge `feature/data-cleaning`** → Contains USAspending yearly workflows
2. **Merge `feature/data-merge`** → Contains FAC_USAspending merge
3. **Do NOT merge `chore/repo-scaffold`** → Too different, would cause conflicts
4. **Close empty branches** → `feature/dashboard`, `feature/modeling-forecast`, `docs/report-and-slides`

---

# PART 2: OPTIMIZED MAIN BRANCH LAYOUT

## Target Structure (Clean, Professional, Judge-Ready)

```
fiscal-patriots/
│
├── README.md                           # Comprehensive project README
├── LICENSE                             # MIT License
├── .gitignore                          # Updated gitignore
│
├── deliverables/                       # 🎯 JUDGE-FACING (Top Priority)
│   ├── README.md                       # Deliverables index
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
│   │   └── Fiscal_Patriots_Report.pdf   # If available
│   ├── slides/
│   │   ├── README.md
│   │   └── Fiscal_Patriots_Presentation.pdf
│   └── video/
│       ├── README.md
│       └── [video link or file]
│
├── data/                               # 📊 ANALYSIS OUTPUTS
│   ├── README.md                       # Data index with descriptions
│   ├── analysis_core/                  # Primary merged outputs
│   │   ├── FAC_USAspending_Merged_Detail.csv
│   │   ├── FAC_USAspending_Summary_By_Tier.csv
│   │   └── FAC_USAspending_Top_10_Red.csv
│   ├── fac/                            # FAC-specific outputs
│   │   ├── FAC_Master_With_Risk_Score.csv
│   │   └── FAC_Risk_Summary_By_Tier.csv
│   ├── sam/                            # SAM exclusion outputs
│   │   └── SAM_Exclusions_with_UEI.csv
│   ├── merged/                         # Cross-system merges
│   │   ├── SAM_FAC_Merged.csv
│   │   └── SAM_USAspending_Merged.csv
│   ├── ml/                             # ML training data
│   │   ├── FAC_ML_Train.csv
│   │   └── FAC_ML_Test.csv
│   └── dictionaries/                   # All data dictionaries
│       ├── FAC_USAspending_Merged_Detail_DD.docx
│       ├── FAC_USAspending_Summary_By_Tier_DD.docx
│       ├── FAC_Master_With_Risk_Score_DD.docx
│       ├── SAM_Master_DD.docx
│       └── USAspending_DD.docx
│
├── pipeline/                           # 🔧 DATA PROCESSING
│   ├── README.md                       # Pipeline overview
│   ├── alteryx/                        # All Alteryx workflows
│   │   ├── FAC_Master_With_Risk_Score.yxmd
│   │   ├── FAC_USAspending_Merged.yxmd
│   │   ├── SAM_Exclusion_Cleaning.yxmd
│   │   ├── SAM_FAC_Merged.yxmd
│   │   └── SAM_USAspending_Merged.yxmd
│   ├── data_contract.md
│   └── inputs_outputs.md
│
├── docs/                               # 📚 DOCUMENTATION
│   ├── README.md                       # Docs index
│   ├── appendix_hubs/                  # Deep-dive documentation
│   │   ├── case_studies/
│   │   ├── data_sources/
│   │   ├── methodology/
│   │   ├── ml/
│   │   ├── regulatory/
│   │   └── scoring/
│   ├── competition/                    # AGA competition materials
│   ├── presentation/                   # Presentation guides
│   └── team/                           # Team coordination
│
├── webapp/                             # 🌐 WEBSITE (Renamed, cleaned)
│   ├── README.md
│   └── index.html                      # Latest version only
│
└── assets/                             # 🖼️ IMAGES & VISUALS
    ├── dashboard.png
    ├── pipeline.png
    └── logo.png                        # If available
```

---

## Key Changes from Current State

| Current | Optimized | Reason |
|---------|-----------|--------|
| `ML model/` | `deliverables/model/` | No spaces, consolidated |
| `webapp development/` | `webapp/` | Shorter, no spaces |
| `pipeline/alteryx workflow (main)/` | `pipeline/alteryx/` | Clean naming |
| 11 webapp HTML files | 1 `index.html` | Only latest needed |
| Data dictionaries scattered | `data/dictionaries/` | Centralized |
| Missing SAM/FAC files | Added to `data/` | Complete dataset |
| `temp` files | Removed | Clean repo |
| No LICENSE | Added MIT | Best practice |

---

## File Count Comparison

| Category | Current Main | Optimized | Change |
|----------|--------------|-----------|--------|
| Root files | 2 | 3 | +1 (LICENSE) |
| deliverables/ | 7 | 12 | +5 (model, video) |
| data/ | 7 | 18 | +11 (SAM, ML, dictionaries) |
| pipeline/ | 4 | 7 | +3 (more workflows) |
| docs/ | 32 | 32 | Same |
| webapp/ | 12 | 2 | -10 (cleanup) |
| assets/ | 2 | 3 | +1 (logo) |
| **TOTAL** | **73** | **~77** | +4 meaningful files |

---

# PART 3: MIGRATION CHECKLIST

## Immediate Actions (Pre-Submission)

- [ ] Rename `ML model/` → move contents to `deliverables/model/`
- [ ] Rename `webapp development/` → `webapp/`
- [ ] Keep only latest webapp HTML, rename to `index.html`
- [ ] Rename `pipeline/alteryx workflow (main)/` → `pipeline/alteryx/`
- [ ] Delete `ML model/temp` file
- [ ] Update root `README.md` with final version
- [ ] Add `FAC_Master_With_Risk_Score.csv` from archive
- [ ] Add `Datathon Predictive Modeling v3.ipynb` to deliverables/model/

## Post-Submission Cleanup

- [ ] Add LICENSE file
- [ ] Consolidate data dictionaries to `data/dictionaries/`
- [ ] Add SAM exclusion outputs
- [ ] Close empty feature branches
- [ ] Archive or delete unused branches

---

# PART 4: README.md FOR MAIN BRANCH

The optimized README.md has been provided separately. Key sections:
- Project overview with live website link
- Why This Exists
- What We Built (5 features)
- Integrated Data Sources (table)
- Key Findings (Prince Hall + Amerihost cases)
- Audit Health Score methodology
- Predictive Modeling Prototype
- Key Datasets & Deliverables
- Repository Structure
- How to Explore / Reproduce
- Team roster
- Disclaimer

---

## Summary

**Current State:** Main branch has good bones but needs cleanup (folder naming, missing files, version clutter)

**Optimized State:** Professional, judge-ready structure with all deliverables accessible in 30 seconds

**Priority Actions:**
1. Fix folder names (remove spaces)
2. Add missing core files (Risk Score CSV/workflow)
3. Clean webapp versions
4. Update README.md

**Time Estimate:** 30-45 minutes for critical fixes
