import requests

from src.config.settings import SPORTSMONKS_API_TOKEN


class SportsMonksFixturesClient:

    BASE_URL = "https://api.sportmonks.com/v3/football"

    def get_fixtures_by_date(self, date: str = "2026-05-17"):
        response = requests.get(
            f"{self.BASE_URL}/fixtures/date/{date}",
            params={
                "api_token": SPORTSMONKS_API_TOKEN,
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()