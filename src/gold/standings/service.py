import pandas as pd

from src.common.postgres import (
    get_postgres_engine,
    create_gold_fact_standings_table,
)
from src.gold.standings.loader import GoldStandingLoader
from src.gold.standings.transformer import GoldStandingTransformer
from src.common.monitoring import log_pipeline_execution

class GoldStandingService:

    def execute(self):
        create_gold_fact_standings_table()

        engine = get_postgres_engine()

        df_silver = pd.read_sql(
            "SELECT * FROM silver.standings",
            con=engine,
        )

        transformer = GoldStandingTransformer()
        df_gold = transformer.transform(df_silver)

        loader = GoldStandingLoader()
        records = loader.load(df_gold)

        log_pipeline_execution(
            pipeline_name="standings",
            layer="gold",
            records_processed=records,
            status="SUCCESS",
            message="Gold standings loaded successfully.",
)

        return {
            "records": records,
            "table": "gold.fact_standings",
        }