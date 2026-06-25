from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.ingestion.teams.service import TeamIngestionService
from src.silver.teams.service import SilverTeamService
from src.gold.teams.service import GoldTeamService


def run_bronze_ingestion():
    result = TeamIngestionService().execute()
    print(result)


def run_silver_transformation():
    result = SilverTeamService().execute()
    print(result)


def run_gold_load():
    result = GoldTeamService().execute()
    print(result)


with DAG(
    dag_id="team_pipeline_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["sportflow", "pipeline", "teams"],
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