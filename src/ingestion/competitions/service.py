from .extractor import CompetitionExtractor
from .minio_storage import MinIOStorage


class CompetitionIngestionService:

    def __init__(self):

        self.extractor = CompetitionExtractor()
        self.storage = MinIOStorage()

    def execute(self):

        competitions = self.extractor.extract()

        object_name = self.storage.save(
            competitions
        )

        return {
            "records": len(competitions),
            "object_name": object_name,
        }