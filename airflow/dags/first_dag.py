
from datetime import datetime
import sys

from airflow.sdk import dag, task

# Make project source code accessible
sys.path.insert(0, "/opt/airflow/project")


@dag(
    dag_id="ecommerce_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["ecommerce", "etl", "learning"]
)
def ecommerce_etl_pipeline():

    @task
    def run_etl():
        from src.pipeline import run_pipeline

        print("Starting Ecommerce ETL Pipeline...")
        run_pipeline()
        print("Ecommerce ETL Pipeline completed successfully!")

    run_etl()


ecommerce_etl_pipeline()
