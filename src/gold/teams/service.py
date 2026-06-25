import pandas as pd

from src.common.postgres import (
    get_postgres_engine,
    create_gold_dim_teams_table,
)
from src.gold.teams.loader import GoldTeamLoader
from src.gold.teams.transformer import GoldTeamTransformer
from src.common.monitoring import log_pipeline_execution


class GoldTeamService:

    def execute(self):
        create_gold_dim_teams_table()

        engine = get_postgres_engine()

        df_silver = pd.read_sql(
            "SELECT * FROM silver.teams",
            con=engine,
        )

        transformer = GoldTeamTransformer()
        df_gold = transformer.transform(df_silver)

        loader = GoldTeamLoader()
        records = loader.load(df_gold)

        log_pipeline_execution(
            pipeline_name="teams",
            layer="gold",
            records_processed=records,
            status="SUCCESS",
            message="Gold teams loaded successfully.",
)

        return {
            "records": records,
            "table": "gold.dim_teams",
        }