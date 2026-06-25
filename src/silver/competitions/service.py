from src.bronze.competitions.reader import BronzeCompetitionReader
from src.silver.competitions.transformer import SilverCompetitionTransformer
from src.silver.competitions.loader import SilverCompetitionLoader
from src.common.postgres import create_silver_competitions_table
from src.common.quality.competitions import (
    validate_competitions,
)


class SilverCompetitionService:

    def execute(self):
        create_silver_competitions_table()

        reader = BronzeCompetitionReader()
        _, data = reader.read_latest()

        transformer = SilverCompetitionTransformer()
        df = transformer.transform(data)

        validate_competitions(df)

        loader = SilverCompetitionLoader()
        records = loader.load(df)

        return {
            "records": records,
            "table": "silver.competitions",
        }