import pandas as pd
from pathlib import Path

raw = Path.cwd() / "data" / "raw"
processed = Path.cwd() / "data" / "processed"

# 1) Load final (no Calendar_Type) and CC map
df_final = pd.read_csv(processed / "fake_data_individual.csv")
cc = pd.read_excel(raw / "Transfer School Calendar Types.xlsx")[["College_Name", "Calendar_Type"]]

# 2) Simple normalization so names match
def norm(s):
    return (s.astype(str).str.upper().str.replace(r"\s+", " ", regex=True).str.strip())

df_final["__join"] = norm(df_final["college_name"])
cc["__join"] = norm(cc["College_Name"])

# 3) Merge and coalesce Calendar_Type
cc_map = cc[["__join","Calendar_Type"]].drop_duplicates("__join")
patched = df_final.merge(cc_map, on="__join", how="left")
patched["Calendar_Type"] = patched["Calendar_Type_x"].fillna(patched["Calendar_Type_y"])
patched = patched.drop(columns=[c for c in patched.columns if c.endswith("_x") or c.endswith("_y")] + ["__join"])

# 4) Save
out = processed / "fake_data_individual_patched.csv"
patched.to_csv(out, index=False)
print("Patched and saved to:", out)
print("Missing Calendar_Type after patch:", int(patched["Calendar_Type"].isna().sum()))





