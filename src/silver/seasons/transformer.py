import pandas as pd


class SilverSeasonTransformer:

    def transform(self, data):
        df = pd.DataFrame(data)

        df = df.rename(
            columns={
                "id": "season_id",
            }
        )

        expected_columns = [
            "season_id",
            "sport_id",
            "league_id",
            "tie_breaker_rule_id",
            "name",
            "finished",
            "pending",
            "is_current",
            "starting_at",
            "ending_at",
            "standings_recalculated_at",
            "games_in_current_week",
        ]

        df = df[expected_columns]

        df["starting_at"] = pd.to_datetime(
            df["starting_at"],
            errors="coerce",
        )

        df["ending_at"] = pd.to_datetime(
            df["ending_at"],
            errors="coerce",
        )

        df["standings_recalculated_at"] = pd.to_datetime(
            df["standings_recalculated_at"],
            errors="coerce",
        )

        return df