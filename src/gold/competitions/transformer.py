class GoldCompetitionTransformer:

    def transform(self, df):
        return df[
            [
                "competition_id",
                "competition_name",
                "country_id",
                "type",
                "sub_type",
                "active",
                "last_played_at",
            ]
        ].copy()