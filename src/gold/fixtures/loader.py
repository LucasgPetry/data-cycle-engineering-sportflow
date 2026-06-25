from src.common.postgres import get_postgres_engine


class GoldFixtureLoader:

    def load(self, df):
        engine = get_postgres_engine()

        df.to_sql(
            name="fact_fixtures",
            con=engine,
            schema="gold",
            if_exists="replace",
            index=False,
        )

        return len(df)