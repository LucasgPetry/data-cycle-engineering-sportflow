import requests

from src.config.settings import SPORTSMONKS_API_TOKEN


class SportsMonksStandingsClient:

    BASE_URL = "https://api.sportmonks.com/v3/football"

    def get_standings_by_season(self, season_id: int = 825):
        response = requests.get(
            f"{self.BASE_URL}/standings/seasons/{season_id}",
            params={
                "api_token": SPORTSMONKS_API_TOKEN,
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()