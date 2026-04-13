# Run from repository root: `make pipeline`
.PHONY: pipeline etl db notebooks

pipeline:
	python scripts/run_pipeline.py

etl:
	python scripts/run_pipeline.py --skip-db

db:
	python scripts/run_pipeline.py --skip-etl

notebooks:
	python scripts/run_pipeline.py --skip-etl --skip-db --execute-notebooks
