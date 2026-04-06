import pathlib

import pandas as pd
from sqlalchemy import create_engine, text
import yaml


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[3]


def load_db_config(env: str = "dev") -> dict:
    config_path = PROJECT_ROOT / "config" / env / "db_config.yaml"
    with config_path.open("r") as f:
        return yaml.safe_load(f)


def make_engine(cfg: dict):
    url = (
        f"postgresql+psycopg2://{cfg['user']}:{cfg['password']}@"
        f"{cfg['host']}:{cfg['port']}/{cfg['database']}"
    )
    return create_engine(url)


def _load_schema_sql() -> str:
    schema_path = PROJECT_ROOT / "src" / "db" / "schema" / "customer_retention_schema.sql"
    return schema_path.read_text()


def _load_full_table_view_sql() -> str:
    view_path = PROJECT_ROOT / "src" / "db" / "schema" / "full_table_view.sql"
    return view_path.read_text()


def recreate_schema(engine) -> None:
    # Views must be dropped before tables they reference (e.g. v_fulltable -> outcomes).
    drops = [
        "DROP VIEW IF EXISTS v_fulltable CASCADE;",
        "DROP TABLE IF EXISTS outcomes;",
        "DROP TABLE IF EXISTS billing;",
        "DROP TABLE IF EXISTS services;",
        "DROP TABLE IF EXISTS customers;",
    ]
    schema_sql = _load_schema_sql()

    with engine.begin() as conn:
        for stmt in drops:
            conn.execute(text(stmt))
        conn.execute(text(schema_sql))


def load_csv(env: str = "dev") -> None:
    cfg = load_db_config(env)
    engine = make_engine(cfg)

    csv_path = PROJECT_ROOT / "data" / "processed" / "churn_data_cleaned.csv"

    df = pd.read_csv(csv_path)

    # Clean column names to match SQL (lowercase, no spaces)
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]

    # Some rows in this dataset have blank TotalCharges; coerce to numeric
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

    # DB column is INTEGER; cleaned CSV may have "Yes"/"No" if ETL mapped it
    sc = df["seniorcitizen"]
    if sc.dtype == object:
        df["seniorcitizen"] = sc.map({"Yes": 1, "No": 0})
    else:
        df["seniorcitizen"] = pd.to_numeric(sc, errors="coerce")
    df["seniorcitizen"] = df["seniorcitizen"].fillna(0).astype(int)

    recreate_schema(engine)

    customers_cols = [
        "customerid",
        "gender",
        "seniorcitizen",
        "partner",
        "dependents",
        "tenure",
    ]
    services_cols = [
        "customerid",
        "phoneservice",
        "multiplelines",
        "internetservice",
        "onlinesecurity",
        "onlinebackup",
        "deviceprotection",
        "techsupport",
        "streamingtv",
        "streamingmovies",
    ]
    billing_cols = [
        "customerid",
        "contract",
        "paperlessbilling",
        "paymentmethod",
        "monthlycharges",
        "totalcharges",
    ]
    outcomes_cols = ["customerid", "churn"]

    df[customers_cols].to_sql("customers", engine, if_exists="append", index=False)
    df[services_cols].to_sql("services", engine, if_exists="append", index=False)
    df[billing_cols].to_sql("billing", engine, if_exists="append", index=False)
    df[outcomes_cols].to_sql("outcomes", engine, if_exists="append", index=False)

    with engine.begin() as conn:
        conn.execute(text(_load_full_table_view_sql()))


if __name__ == "__main__":
    load_csv()
