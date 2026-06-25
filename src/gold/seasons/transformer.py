class GoldSeasonTransformer:

    def transform(self, df):
        df_gold = df[
            [
                "season_id",
                "league_id",
                "name",
                "is_current",
                "finished",
                "starting_at",
                "ending_at",
            ]
        ].copy()

        df_gold = df_gold.rename(
            columns={
                "name": "season_name",
            }
        )

        return df_gold