class GoldStandingTransformer:

    def transform(self, df):
        return df[
            [
                "standing_id",
                "participant_id",
                "league_id",
                "season_id",
                "stage_id",
                "position",
                "points",
                "result",
            ]
        ].copy()