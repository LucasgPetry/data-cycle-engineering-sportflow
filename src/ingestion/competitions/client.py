import requests

from src.config.settings import SPORTSMONKS_API_TOKEN


class SportsMonksClient:

    BASE_URL = "https://api.sportmonks.com/v3/football"

    def get_leagues(self):

        response = requests.get(
            f"{self.BASE_URL}/leagues",
            params={
                "api_token": SPORTSMONKS_API_TOKEN
            },
            timeout=30
        )

        response.raise_for_status()

        return response.json()