import pandas as pd


def validate_teams(
    dataframe: pd.DataFrame,
):

    if dataframe["team_id"].isnull().any():
        raise ValueError(
            "Team ID contains null values."
        )

    if dataframe["team_name"].isnull().any():
        raise ValueError(
            "Team name contains null values."
        )

    duplicates = dataframe[
        "team_id"
    ].duplicated().sum()

    if duplicates > 0:
        raise ValueError(
            f"Found {duplicates} duplicated teams."
        )

    return True