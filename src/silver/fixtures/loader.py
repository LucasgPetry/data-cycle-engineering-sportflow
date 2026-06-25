from src.common.postgres import get_postgres_engine


class SilverFixtureLoader:

    def load(self, df):
        engine = get_postgres_engine()

        df.to_sql(
            name="fixtures",
            con=engine,
            schema="silver",
            if_exists="replace",
            index=False,
        )

        return len(df)