from src.ingestion.teams.client import SportsMonksTeamsClient


class TeamExtractor:

    def __init__(self):
        self.client = SportsMonksTeamsClient()

    def extract(self):

        all_teams = []

        COUNTRY_IDS = [
            320,
            1161,
            462,
            5,
            38,
            32,
            251,
            404,
        ]

        for country_id in COUNTRY_IDS:

            response = self.client.get_teams_by_country(
                country_id=country_id
            )

            teams = response["data"]

            all_teams.extend(teams)

            print(
                f"Country {country_id}: "
                f"{len(teams)} teams"
            )

        return all_teams