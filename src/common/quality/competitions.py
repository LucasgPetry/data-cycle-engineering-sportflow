import pandas as pd


def validate_competitions(
    dataframe: pd.DataFrame,
):

    if dataframe["competition_id"].isnull().any():
        raise ValueError(
            "Competition ID contains null values."
        )

    if dataframe["competition_name"].isnull().any():
        raise ValueError(
            "Competition name contains null values."
        )

    duplicates = dataframe[
        "competition_id"
    ].duplicated().sum()

    if duplicates > 0:
        raise ValueError(
            f"Found {duplicates} duplicated competitions."
        )

    return True