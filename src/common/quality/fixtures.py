import pandas as pd


def validate_fixtures(
    dataframe: pd.DataFrame,
):

    if dataframe["fixture_id"].isnull().any():
        raise ValueError(
            "Fixture ID contains null values."
        )

    if dataframe["season_id"].isnull().any():
        raise ValueError(
            "Season ID contains null values."
        )

    duplicates = dataframe[
        "fixture_id"
    ].duplicated().sum()

    if duplicates > 0:
        raise ValueError(
            f"Found {duplicates} duplicated fixtures."
        )

    return True