import pandas as pd


class SilverFixtureTransformer:

    def transform(self, data):
        df = pd.DataFrame(data)

        df = df.rename(
            columns={
                "id": "fixture_id",
            }
        )

        expected_columns = [
            "fixture_id",
            "sport_id",
            "league_id",
            "season_id",
            "stage_id",
            "group_id",
            "aggregate_id",
            "round_id",
            "state_id",
            "venue_id",
            "name",
            "starting_at",
            "result_info",
            "leg",
            "details",
            "length",
            "placeholder",
            "has_odds",
            "has_premium_odds",
            "starting_at_timestamp",
        ]

        df = df[expected_columns]

        df["starting_at"] = pd.to_datetime(
            df["starting_at"],
            errors="coerce",
        )

        return df