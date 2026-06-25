from src.bronze.standings.reader import BronzeStandingReader
from src.common.postgres import create_silver_standings_table
from src.silver.standings.loader import SilverStandingLoader
from src.silver.standings.transformer import SilverStandingTransformer
from src.common.quality.standings import (
    validate_standings,
)

class SilverStandingService:

    def execute(self):
        create_silver_standings_table()

        reader = BronzeStandingReader()
        _, data = reader.read_latest()

        transformer = SilverStandingTransformer()
        df = transformer.transform(data)

        validate_standings(df)

        loader = SilverStandingLoader()
        records = loader.load(df)

        return {
            "records": records,
            "table": "silver.standings",
        }