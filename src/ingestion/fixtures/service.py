from src.ingestion.fixtures.extractor import FixtureExtractor
from src.ingestion.fixtures.minio_storage import FixtureMinIOStorage


class FixtureIngestionService:

    def __init__(self):
        self.extractor = FixtureExtractor()
        self.storage = FixtureMinIOStorage()

    def execute(self):
        fixtures = self.extractor.extract()

        object_name = self.storage.save(fixtures)

        return {
            "records": len(fixtures),
            "object_name": object_name,
        }