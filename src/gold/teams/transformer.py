class GoldTeamTransformer:

    def transform(self, df):
        return df[
            [
                "team_id",
                "team_name",
                "country_id",
                "venue_id",
                "gender",
                "type",
                "founded",
                "last_played_at",
            ]
        ].copy()