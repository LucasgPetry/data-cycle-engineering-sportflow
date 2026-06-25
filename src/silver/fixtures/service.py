from src.bronze.fixtures.reader import BronzeFixtureReader
from src.common.postgres import create_silver_fixtures_table
from src.silver.fixtures.loader import SilverFixtureLoader
from src.silver.fixtures.transformer import SilverFixtureTransformer
from src.common.quality.fixtures import (
    validate_fixtures,
)


class SilverFixtureService:

    def execute(self):
        create_silver_fixtures_table()

        reader = BronzeFixtureReader()
        _, data = reader.read_latest()

        transformer = SilverFixtureTransformer()
        df = transformer.transform(data)

        validate_fixtures(df)

        loader = SilverFixtureLoader()
        records = loader.load(df)

        return {
            "records": records,
            "table": "silver.fixtures",
        }