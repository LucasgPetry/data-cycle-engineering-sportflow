import pandas as pd

from src.common.postgres import (
    get_postgres_engine,
    create_gold_dim_competitions_table,
)
from src.gold.competitions.transformer import GoldCompetitionTransformer
from src.gold.competitions.loader import GoldCompetitionLoader
from src.common.monitoring import log_pipeline_execution


class GoldCompetitionService:

    def execute(self):
        create_gold_dim_competitions_table()

        engine = get_postgres_engine()

        df_silver = pd.read_sql(
            "SELECT * FROM silver.competitions",
            con=engine,
        )

        transformer = GoldCompetitionTransformer()
        df_gold = transformer.transform(df_silver)

        loader = GoldCompetitionLoader()
        records = loader.load(df_gold)

        log_pipeline_execution(
            pipeline_name="competitions",
            layer="gold",
            records_processed=records,
            status="SUCCESS",
            message="Gold competitions loaded successfully.",
)

        return {
            "records": records,
            "table": "gold.dim_competitions",
        }