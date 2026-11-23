
from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="first_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["learning"]
)
def first_dag():

    @task
    def hello():
        print("Hello! My first Airflow DAG is running.")

    @task
    def extract():
        print("Extracting data...")

    @task
    def transform():
        print("Transforming data...")

    @task
    def load():
        print("Loading data into database...")

    hello() >> extract() >> transform() >> load()


first_dag()
