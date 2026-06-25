from src.ingestion.seasons.client import SportsMonksSeasonsClient


class SeasonExtractor:

    def __init__(self):
        self.client = SportsMonksSeasonsClient()

    def extract(self):
        response = self.client.get_seasons()
        return response["data"]