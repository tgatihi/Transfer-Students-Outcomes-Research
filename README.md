# Transfer Systems ROI — VS Code Starter

This repo scaffolds your analysis comparing **quarterly vs. semester community college transfers** and their **returns** after graduating from a 4‑year university.

## 1) Prereqs
- Install **Python 3.10+**
- Install **VS Code** + extensions: *Python*, *Jupyter*

## 2) Create and activate a virtual environment
```bash
cd cc_transfers_vscode_starter
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 3) Put your data
Copy your Excel file into `data/raw/` (e.g., `data/raw/transfers.xlsx`).

## 4) Open in VS Code
- Open this folder in VS Code
- Select the `.venv` interpreter (bottom-right status bar)
- Open **notebooks/01_explore.ipynb** (or create it) or run **src/run_analysis.py**

## 5) Recommended analysis flow
1. **Define outcome(s)** for "returns": ideally post-grad earnings/employment; if not available, use proxies (time to degree, extra quarters, GPA, graduation within 4 or 6 years).  
2. **Define treatment**: indicator = 1 if *semester CC*, 0 if *quarter CC* (or vice versa).  
3. **Controls**:
   - Demographics: age, gender, race/ethnicity, first‑gen, Pell
   - Academic prep: HS GPA, SAT/ACT, transfer GPA/units
   - Program: major, STEM flag
   - Institutional & time: destination campus fixed effects, entry cohort year
4. **EDA**: check missingness, distributions, balance between systems.
5. **Model**: OLS on log earnings or linear probability for employment; robust SEs. Add campus & cohort fixed effects.
6. **Robustness**: propensity score weighting/matching; subgroups (STEM vs non‑STEM; Pell vs non‑Pell).

See `src/run_analysis.py` for a starting script that inspects your columns and generates a variables overview.
