from src.bronze.seasons.reader import BronzeSeasonReader
from src.common.postgres import create_silver_seasons_table
from src.silver.seasons.loader import SilverSeasonLoader
from src.silver.seasons.transformer import SilverSeasonTransformer


class SilverSeasonService:

    def execute(self):
        create_silver_seasons_table()

        reader = BronzeSeasonReader()
        _, data = reader.read_latest()

        transformer = SilverSeasonTransformer()
        df = transformer.transform(data)

        loader = SilverSeasonLoader()
        records = loader.load(df)

        return {
            "records": records,
            "table": "silver.seasons",
        }