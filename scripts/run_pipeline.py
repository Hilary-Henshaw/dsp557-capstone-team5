#!/usr/bin/env python3
"""
Run project pipeline steps from the repository root.

  python scripts/run_pipeline.py              # ETL + load Postgres (needs DB config + server)
  python scripts/run_pipeline.py --skip-db    # ETL only
  python scripts/run_pipeline.py --execute-notebooks   
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run(cmd: list[str], *, cwd: Path) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=str(cwd), check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run capstone ETL / DB / optional notebooks.")
    parser.add_argument("--skip-etl", action="store_true", help="Skip CSV cleaning step.")
    parser.add_argument("--skip-db", action="store_true", help="Skip Postgres load (schema + v_fullTable).")
    parser.add_argument(
        "--execute-notebooks",
        action="store_true",
        help="Execute notebooks with jupyter nbconvert (install jupyter if missing).",
    )
    args = parser.parse_args()

    root = repo_root()
    py = sys.executable

    if not args.skip_etl:
        run([py, str(root / "src" / "etl" / "clean_data.py")], cwd=root)

    if not args.skip_db:
        run([py, str(root / "src" / "db" / "loaders" / "load_customer_retention_db.py")], cwd=root)

    if args.execute_notebooks:
        notebooks = [
            root / "notebooks" / "exploration" / "kn_data_exploration.ipynb",
            root / "notebooks" / "modeling" / "kn_model_training.ipynb",
            root / "ML_Models" / "cleaneddataconvertcode.ipynb",
            root / "ML Models" / "ML_predict.ipynb",
        ]
        for nb in notebooks:
            if not nb.is_file():
                print(f"skip (missing): {nb}", flush=True)
                continue
            run(
                [py, "-m", "nbconvert", "--to", "notebook", "--execute", "--inplace", str(nb)],
                cwd=root,
            )

    print("Pipeline finished.", flush=True)


if __name__ == "__main__":
    main()
