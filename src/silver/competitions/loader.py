from src.common.postgres import get_postgres_engine


class SilverCompetitionLoader:

    def load(self, df):
        engine = get_postgres_engine()

        df.to_sql(
            name="competitions",
            con=engine,
            schema="silver",
            if_exists="replace",
            index=False,
        )

        return len(df)