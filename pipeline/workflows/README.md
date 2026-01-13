# Workflows

This folder documents workflow structure and where to find processing steps.

## Main branch
- Core workflow artifact:
  - `pipeline/alteryx/FAC_USAspending_Merged.yxmd`
- Supporting documentation:
  - `pipeline/inputs_outputs.md`
  - `pipeline/data_contract.md`

## Feature branches
Work-in-progress pipelines and datasets are organized by branch:
- `feature/data-intake`
- `feature/data-cleaning`
- `feature/data-merge`
- `feature/modeling-forecast`
- `feature/dashboard`

Main stays clean and contains only the validated pipeline artifact(s) and analysis core outputs.
