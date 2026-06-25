import pandas as pd

from src.common.postgres import get_postgres_engine
from src.ingestion.standings.client import SportsMonksStandingsClient


class StandingExtractor:

    def __init__(self):
        self.client = SportsMonksStandingsClient()

    def get_season_ids(self):
        engine = get_postgres_engine()

        query = """
            SELECT season_id
            FROM silver.seasons
            ORDER BY season_id
        """

        df = pd.read_sql(query, con=engine)

        return df["season_id"].dropna().astype(int).tolist()

    def extract(self):
        all_standings = []

        season_ids = self.get_season_ids()

        for season_id in season_ids:
            response = self.client.get_standings_by_season(
                season_id=season_id
            )

            standings = response["data"]

            print(
                f"Season {season_id}: {len(standings)} standings"
            )

            all_standings.extend(standings)

        return all_standings