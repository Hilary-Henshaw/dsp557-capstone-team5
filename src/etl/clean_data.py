import pathlib

import pandas as pd


def clean_data(data_path, dest_path):
    churn_data = pd.read_csv(data_path)
    churn_data["TotalCharges"] = pd.to_numeric(churn_data["TotalCharges"], errors="coerce")
    churn_data["MonthlyCharges"] = pd.to_numeric(churn_data["MonthlyCharges"], errors="coerce")
    # Keep SeniorCitizen as 0/1 so Postgres INTEGER and loaders stay aligned
    churn_data["SeniorCitizen"] = (
        pd.to_numeric(churn_data["SeniorCitizen"], errors="coerce").fillna(0).astype(int)
    )
    churn_data = churn_data.dropna(subset=["TotalCharges"])
    churn_data.to_csv(dest_path, index=False)
    print(f"Cleaned dataset saved as {dest_path}")


if __name__ == "__main__":
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    data_path = repo_root / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    dest_path = repo_root / "data" / "processed" / "churn_data_cleaned.csv"
    clean_data(str(data_path), str(dest_path))
