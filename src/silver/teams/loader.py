from src.common.postgres import get_postgres_engine


class SilverTeamLoader:

    def load(self, df):
        engine = get_postgres_engine()

        df.to_sql(
            name="teams",
            con=engine,
            schema="silver",
            if_exists="replace",
            index=False,
        )

        return len(df)