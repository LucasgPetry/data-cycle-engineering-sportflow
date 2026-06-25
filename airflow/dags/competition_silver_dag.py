from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.silver.competitions.service import SilverCompetitionService


def run_competition_silver():
    result = SilverCompetitionService().execute()
    print(result)


with DAG(
    dag_id="competition_silver_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["sportflow", "silver", "competitions"],
) as dag:

    transform_to_silver = PythonOperator(
        task_id="transform_competitions_to_silver",
        python_callable=run_competition_silver,
    )