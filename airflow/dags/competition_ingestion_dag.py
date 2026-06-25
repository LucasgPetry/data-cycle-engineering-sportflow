from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.ingestion.competitions.service import (
    CompetitionIngestionService,
)


def run_competition_ingestion():

    result = (
        CompetitionIngestionService()
        .execute()
    )

    print(result)


with DAG(
    dag_id="competition_ingestion_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["sportflow", "bronze", "competitions"],
) as dag:

    ingest_competitions = PythonOperator(
        task_id="ingest_competitions",
        python_callable=run_competition_ingestion,
    )