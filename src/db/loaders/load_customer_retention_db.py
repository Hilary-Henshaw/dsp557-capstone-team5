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


def recreate_schema(engine) -> None:
    # Drop child tables first due to FKs
    drops = [
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

    csv_path = PROJECT_ROOT / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

    df = pd.read_csv(csv_path)

    # Clean column names to match SQL (lowercase, no spaces)
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]

    # Some rows in this dataset have blank TotalCharges; coerce to numeric
    df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

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


if __name__ == "__main__":
    load_csv()
