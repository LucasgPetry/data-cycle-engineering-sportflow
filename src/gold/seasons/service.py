import pandas as pd

from src.common.postgres import (
    get_postgres_engine,
    create_gold_dim_seasons_table,
)
from src.gold.seasons.loader import GoldSeasonLoader
from src.gold.seasons.transformer import GoldSeasonTransformer
from src.common.monitoring import log_pipeline_execution


class GoldSeasonService:

    def execute(self):
        create_gold_dim_seasons_table()

        engine = get_postgres_engine()

        df_silver = pd.read_sql(
            "SELECT * FROM silver.seasons",
            con=engine,
        )

        transformer = GoldSeasonTransformer()
        df_gold = transformer.transform(df_silver)

        loader = GoldSeasonLoader()
        records = loader.load(df_gold)

        log_pipeline_execution(
            pipeline_name="seasons",
            layer="gold",
            records_processed=records,
            status="SUCCESS",
            message="Gold seasons loaded successfully.",
)

        return {
            "records": records,
            "table": "gold.dim_seasons",
        }