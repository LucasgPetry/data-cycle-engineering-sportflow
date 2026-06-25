import pandas as pd


class SilverTeamTransformer:

    def transform(self, data):
        df = pd.DataFrame(data)

        df = df.rename(
            columns={
                "id": "team_id",
                "name": "team_name",
            }
        )

        expected_columns = [
            "team_id",
            "sport_id",
            "country_id",
            "venue_id",
            "gender",
            "team_name",
            "short_code",
            "image_path",
            "founded",
            "type",
            "placeholder",
            "last_played_at",
        ]

        df = df[expected_columns]

        df["last_played_at"] = pd.to_datetime(
            df["last_played_at"],
            errors="coerce",
        )

        return df