import pandas as pd


class SilverCompetitionTransformer:

    def transform(self, data):
        df = pd.DataFrame(data)

        df = df.rename(
            columns={
                "id": "competition_id",
                "name": "competition_name",
            }
        )

        expected_columns = [
            "competition_id",
            "sport_id",
            "country_id",
            "competition_name",
            "short_code",
            "type",
            "sub_type",
            "category",
            "active",
            "has_jerseys",
            "image_path",
            "last_played_at",
        ]

        df = df[expected_columns]

        df["last_played_at"] = pd.to_datetime(
            df["last_played_at"],
            errors="coerce",
        )

        return df