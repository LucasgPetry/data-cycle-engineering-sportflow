class GoldFixtureTransformer:

    def transform(self, df):
        df_gold = df[
            [
                "fixture_id",
                "league_id",
                "season_id",
                "venue_id",
                "state_id",
                "name",
                "starting_at",
                "result_info",
                "has_odds",
            ]
        ].copy()

        df_gold = df_gold.rename(
            columns={
                "name": "fixture_name",
            }
        )

        return df_gold