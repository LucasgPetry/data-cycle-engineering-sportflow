from src.common.postgres import get_postgres_engine


class SilverStandingLoader:

    def load(self, df):
        engine = get_postgres_engine()

        df.to_sql(
            name="standings",
            con=engine,
            schema="silver",
            if_exists="replace",
            index=False,
        )

        return len(df)