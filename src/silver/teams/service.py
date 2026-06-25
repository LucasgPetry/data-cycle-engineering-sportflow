from src.bronze.teams.reader import BronzeTeamReader
from src.common.postgres import create_silver_teams_table
from src.silver.teams.loader import SilverTeamLoader
from src.silver.teams.transformer import SilverTeamTransformer
from src.common.quality.teams import (
    validate_teams,
)


class SilverTeamService:

    def execute(self):
        create_silver_teams_table()

        reader = BronzeTeamReader()
        _, data = reader.read_latest()

        transformer = SilverTeamTransformer()
        df = transformer.transform(data)

        validate_teams(df)

        loader = SilverTeamLoader()
        records = loader.load(df)

        return {
            "records": records,
            "table": "silver.teams",
        }