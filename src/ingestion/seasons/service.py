from src.ingestion.seasons.extractor import SeasonExtractor
from src.ingestion.seasons.minio_storage import SeasonMinIOStorage


class SeasonIngestionService:

    def __init__(self):
        self.extractor = SeasonExtractor()
        self.storage = SeasonMinIOStorage()

    def execute(self):
        seasons = self.extractor.extract()

        object_name = self.storage.save(seasons)

        return {
            "records": len(seasons),
            "object_name": object_name,
        }