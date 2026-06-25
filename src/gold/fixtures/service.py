import pandas as pd

from src.common.postgres import (
    get_postgres_engine,
    create_gold_fact_fixtures_table,
)
from src.gold.fixtures.loader import GoldFixtureLoader
from src.gold.fixtures.transformer import GoldFixtureTransformer
from src.common.monitoring import log_pipeline_execution


class GoldFixtureService:

    def execute(self):
        create_gold_fact_fixtures_table()

        engine = get_postgres_engine()

        df_silver = pd.read_sql(
            "SELECT * FROM silver.fixtures",
            con=engine,
        )

        transformer = GoldFixtureTransformer()
        df_gold = transformer.transform(df_silver)

        loader = GoldFixtureLoader()
        records = loader.load(df_gold)

        log_pipeline_execution(
            pipeline_name="fixtures",
            layer="gold",
            records_processed=records,
            status="SUCCESS",
            message="Gold fixtures loaded successfully.",
)

        return {
            "records": records,
            "table": "gold.fact_fixtures",
        }