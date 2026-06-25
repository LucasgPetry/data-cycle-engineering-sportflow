from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.ingestion.competitions.service import CompetitionIngestionService
from src.silver.competitions.service import SilverCompetitionService
from src.gold.competitions.service import GoldCompetitionService

from src.ingestion.teams.service import TeamIngestionService
from src.silver.teams.service import SilverTeamService
from src.gold.teams.service import GoldTeamService

from src.ingestion.seasons.service import SeasonIngestionService
from src.silver.seasons.service import SilverSeasonService
from src.gold.seasons.service import GoldSeasonService

from src.ingestion.fixtures.service import FixtureIngestionService
from src.silver.fixtures.service import SilverFixtureService
from src.gold.fixtures.service import GoldFixtureService

from src.ingestion.standings.service import StandingIngestionService
from src.silver.standings.service import SilverStandingService
from src.gold.standings.service import GoldStandingService


def run_competitions_bronze():
    print(CompetitionIngestionService().execute())


def run_competitions_silver():
    print(SilverCompetitionService().execute())


def run_competitions_gold():
    print(GoldCompetitionService().execute())


def run_teams_bronze():
    print(TeamIngestionService().execute())


def run_teams_silver():
    print(SilverTeamService().execute())


def run_teams_gold():
    print(GoldTeamService().execute())


def run_seasons_bronze():
    print(SeasonIngestionService().execute())


def run_seasons_silver():
    print(SilverSeasonService().execute())


def run_seasons_gold():
    print(GoldSeasonService().execute())


def run_fixtures_bronze():
    print(FixtureIngestionService().execute())


def run_fixtures_silver():
    print(SilverFixtureService().execute())


def run_fixtures_gold():
    print(GoldFixtureService().execute())


def run_standings_bronze():
    print(StandingIngestionService().execute())


def run_standings_silver():
    print(SilverStandingService().execute())


def run_standings_gold():
    print(GoldStandingService().execute())


with DAG(
    dag_id="sportflow_master_pipeline_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["sportflow", "master", "pipeline"],
) as dag:

    competitions_bronze = PythonOperator(
        task_id="competitions_bronze",
        python_callable=run_competitions_bronze,
    )

    competitions_silver = PythonOperator(
        task_id="competitions_silver",
        python_callable=run_competitions_silver,
    )

    competitions_gold = PythonOperator(
        task_id="competitions_gold",
        python_callable=run_competitions_gold,
    )

    teams_bronze = PythonOperator(
        task_id="teams_bronze",
        python_callable=run_teams_bronze,
    )

    teams_silver = PythonOperator(
        task_id="teams_silver",
        python_callable=run_teams_silver,
    )

    teams_gold = PythonOperator(
        task_id="teams_gold",
        python_callable=run_teams_gold,
    )

    seasons_bronze = PythonOperator(
        task_id="seasons_bronze",
        python_callable=run_seasons_bronze,
    )

    seasons_silver = PythonOperator(
        task_id="seasons_silver",
        python_callable=run_seasons_silver,
    )

    seasons_gold = PythonOperator(
        task_id="seasons_gold",
        python_callable=run_seasons_gold,
    )

    fixtures_bronze = PythonOperator(
        task_id="fixtures_bronze",
        python_callable=run_fixtures_bronze,
    )

    fixtures_silver = PythonOperator(
        task_id="fixtures_silver",
        python_callable=run_fixtures_silver,
    )

    fixtures_gold = PythonOperator(
        task_id="fixtures_gold",
        python_callable=run_fixtures_gold,
    )

    standings_bronze = PythonOperator(
        task_id="standings_bronze",
        python_callable=run_standings_bronze,
    )

    standings_silver = PythonOperator(
        task_id="standings_silver",
        python_callable=run_standings_silver,
    )

    standings_gold = PythonOperator(
        task_id="standings_gold",
        python_callable=run_standings_gold,
    )

    competitions_bronze >> competitions_silver >> competitions_gold
    teams_bronze >> teams_silver >> teams_gold
    seasons_bronze >> seasons_silver >> seasons_gold
    fixtures_bronze >> fixtures_silver >> fixtures_gold
    standings_bronze >> standings_silver >> standings_gold