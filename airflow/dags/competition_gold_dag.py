from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.gold.competitions.service import GoldCompetitionService


def run_competition_gold():
    result = GoldCompetitionService().execute()
    print(result)


with DAG(
    dag_id="competition_gold_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["sportflow", "gold", "competitions"],
) as dag:

    load_gold = PythonOperator(
        task_id="load_competitions_gold",
        python_callable=run_competition_gold,
    )