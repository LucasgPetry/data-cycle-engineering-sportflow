from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.ingestion.seasons.service import SeasonIngestionService
from src.silver.seasons.service import SilverSeasonService
from src.gold.seasons.service import GoldSeasonService


def run_bronze_ingestion():
    result = SeasonIngestionService().execute()
    print(result)


def run_silver_transformation():
    result = SilverSeasonService().execute()
    print(result)


def run_gold_load():
    result = GoldSeasonService().execute()
    print(result)


with DAG(
    dag_id="season_pipeline_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["sportflow", "pipeline", "seasons"],
) as dag:

    bronze_ingestion = PythonOperator(
        task_id="bronze_ingestion",
        python_callable=run_bronze_ingestion,
    )

    silver_transformation = PythonOperator(
        task_id="silver_transformation",
        python_callable=run_silver_transformation,
    )

    gold_load = PythonOperator(
        task_id="gold_load",
        python_callable=run_gold_load,
    )

    bronze_ingestion >> silver_transformation >> gold_load