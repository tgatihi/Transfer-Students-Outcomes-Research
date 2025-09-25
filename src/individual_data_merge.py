import pandas as pd
from pathlib import Path

# Paths
raw_path = Path.cwd() / "data" / "raw"
processed_path = Path.cwd() / "data" / "processed"
processed_path.mkdir(parents=True, exist_ok=True)

# Load data
df_main = pd.read_excel(raw_path / "fake_data.xlsx")
df_calendar = pd.read_excel(raw_path / "Transfer School Calendar Types.xlsx")

# Merge with calendar type info
df_main_with_calendar = df_main.merge(
    df_calendar,
    left_on="college_name",
    right_on="College_Name",
    how="left"
)

# Collapse to individual-level (one row per ID)
df_individual = df_main_with_calendar.groupby("ID").agg({
    "Calendar_Type": "first",
    "CC_transfer": "first",
    "final_GPA": "last",
    "time_to_grad": "last",
    "extra_quarters": "last",
    "grad_on_time": "last",
    "graduated": "last",
    "total_units": "last",
    "gender": "first",
    "uc_ethnicity": "first",
    "first_gen_bachelors": "first",
    "ever_pell_fl": "first",
    "age_at_grad": "first",
    "CC_GPA_standard": "first",
    "entry_year": "first",
    "college_name": "first"
}).reset_index()

# Save processed dataset
df_individual.to_csv(processed_path / "fake_data_individual.csv", index=False)

print("Finished! Individual-level dataset saved at:", processed_path / "fake_data_individual.csv")




