from .client import SportsMonksClient


class CompetitionExtractor:

    def __init__(self):
        self.client = SportsMonksClient()

    def extract(self):

        response = self.client.get_leagues()

        return response["data"]