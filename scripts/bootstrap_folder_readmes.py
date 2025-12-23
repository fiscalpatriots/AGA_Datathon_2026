#!/usr/bin/env python3
from pathlib import Path

FILES = {
    ".github/README.txt": "GitHub configuration files (templates, CODEOWNERS, CI workflows).",
    ".github/workflows/README.txt": "Automation that runs on GitHub (checks/tests on pull requests).",

    "configs/README.txt": "Project configuration files (use-case settings, parameters, dataset choices).",

    "docs/README.txt": "Project documentation for the team and judges (sources, methodology, definitions).",
    "docs/meeting_notes/README.txt": "Meeting notes and decisions, named by date (YYYY-MM-DD).",

    "data/README.txt": (
        "Data handling rules.\n"
        "Do NOT store large raw datasets in GitHub.\n"
        "Only store small samples and documentation. Full data lives in shared storage (e.g., OneDrive/S3).\n"
    ),
    "data/samples/README.txt": "Small sample datasets for testing scripts and Tableau connections (safe to commit).",

    "src/README.txt": "All source code for the data pipeline, modeling, and visualization preparation.",
    "src/ingest/README.txt": "Scripts that pull/download raw data from APIs or files into raw storage.",
    "src/clean/README.txt": "Scripts that clean/standardize each dataset (types, columns, missing values, keys).",
    "src/merge/README.txt": "Scripts that merge datasets into one analysis-ready table (usually keyed by state + year).",
    "src/features/README.txt": "Compute derived metrics (per-capita spend, ROI-style metrics, deltas pre/post policy).",
    "src/modeling/README.txt": "Forecasting and scenario logic for the tool (baseline and what-if calculations).",
    "src/validate/README.txt": "Sanity checks (missing values, duplicates, expected states/years, value ranges).",
    "src/viz/README.txt": "Prep outputs for visuals (Tableau-ready exports, summary tables, chart-ready slices).",

    "notebooks/README.txt": (
        "Exploratory notebooks and prototypes.\n"
        "Notebooks are optional; final logic should be in src/ and scripts/ for reproducibility.\n"
    ),

    "reports/README.txt": "Generated outputs for write-ups and submission packaging (figures, tables, final artifacts).",
    "reports/figures/README.txt": "Saved charts/plots used in the final narrative and presentation materials.",
    "reports/tables/README.txt": "Exported tables used in the final narrative and presentation materials.",
    "reports/final_submission/README.txt": (
        "Final submission packaging:\n"
        "- final links (dashboard/video)\n"
        "- final figures/tables exports\n"
        "- last-mile notes for submission\n"
    ),

    "dashboard/README.txt": "Dashboard deliverables (Tableau assets and optional embedded web page).",
    "dashboard/tableau/README.txt": (
        "Tableau dashboard assets.\n"
        "Keep instructions here: required data file name/columns and how to open/publish the workbook.\n"
    ),
    "dashboard/tableau/workbook/README.txt": (
        "Place the Tableau workbook here only if it is small enough.\n"
        "If too large, store externally and put a link + instructions in dashboard/tableau/README.txt.\n"
    ),
    "dashboard/web_embed/README.txt": (
        "Optional: a tiny web page that embeds the published Tableau dashboard.\n"
        "Can be hosted later (e.g., AWS Amplify/S3) to provide a single 'tool link'.\n"
    ),

    "infra/README.txt": "Optional infrastructure notes and deployment artifacts (only if we deploy anything).",
    "infra/aws/README.txt": "Optional AWS plan (S3 dataset storage, hosting, or minimal serverless endpoints).",

    "scripts/README.txt": "Entry-point scripts (one-command runs) to build datasets and run validations.",
}

def write_file(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")

def main():
    repo_root = Path(".").resolve()
    created = 0
    for rel, content in FILES.items():
        p = repo_root / rel
        if not p.exists():
            write_file(p, content)
            created += 1
    print(f"Done. Created {created} README.txt files.")
    print("Tip: you can edit any README.txt later without breaking the structure.")

if __name__ == "__main__":
    main()

