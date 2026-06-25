from src.ingestion.teams.extractor import TeamExtractor
from src.ingestion.teams.minio_storage import TeamMinIOStorage


class TeamIngestionService:

    def __init__(self):
        self.extractor = TeamExtractor()
        self.storage = TeamMinIOStorage()

    def execute(self):
        teams = self.extractor.extract()

        object_name = self.storage.save(teams)

        return {
            "records": len(teams),
            "object_name": object_name,
        }