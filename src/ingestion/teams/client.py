import requests

from src.config.settings import SPORTSMONKS_API_TOKEN


class SportsMonksTeamsClient:

    BASE_URL = "https://api.sportmonks.com/v3/football"

    def get_teams_by_country(self, country_id: int = 320):
        response = requests.get(
            f"{self.BASE_URL}/teams/countries/{country_id}",
            params={
                "api_token": SPORTSMONKS_API_TOKEN,
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()