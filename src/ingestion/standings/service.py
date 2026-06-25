from src.ingestion.standings.extractor import StandingExtractor
from src.ingestion.standings.minio_storage import StandingMinIOStorage


class StandingIngestionService:

    def __init__(self):
        self.extractor = StandingExtractor()
        self.storage = StandingMinIOStorage()

    def execute(self):
        standings = self.extractor.extract()

        object_name = self.storage.save(standings)

        return {
            "records": len(standings),
            "object_name": object_name,
        }