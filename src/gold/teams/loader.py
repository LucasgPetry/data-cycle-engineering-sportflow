from src.common.postgres import get_postgres_engine


class GoldTeamLoader:

    def load(self, df):
        engine = get_postgres_engine()

        df.to_sql(
            name="dim_teams",
            con=engine,
            schema="gold",
            if_exists="replace",
            index=False,
        )

        return len(df)