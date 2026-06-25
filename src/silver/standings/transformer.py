import pandas as pd


class SilverStandingTransformer:

    def transform(self, data):
        df = pd.DataFrame(data)

        df = df.rename(
            columns={
                "id": "standing_id",
            }
        )

        expected_columns = [
            "standing_id",
            "participant_id",
            "sport_id",
            "league_id",
            "season_id",
            "stage_id",
            "group_id",
            "round_id",
            "standing_rule_id",
            "position",
            "result",
            "points",
        ]

        df = df[expected_columns]

        return df