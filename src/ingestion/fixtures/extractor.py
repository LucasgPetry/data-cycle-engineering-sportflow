from datetime import date, timedelta

from src.ingestion.fixtures.client import SportsMonksFixturesClient


class FixtureExtractor:

    def __init__(self):
        self.client = SportsMonksFixturesClient()

    def extract(self):

        all_fixtures = []

        start_date = date(2026, 5, 1)
        end_date = date(2026, 5, 30)

        current_date = start_date

        while current_date <= end_date:

            date_str = current_date.strftime("%Y-%m-%d")

            response = self.client.get_fixtures_by_date(
                date=date_str
            )

            fixtures = response["data"]

            print(
                f"{date_str}: {len(fixtures)} fixtures"
            )

            all_fixtures.extend(fixtures)

            current_date += timedelta(days=1)

        return all_fixtures