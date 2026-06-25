import pandas as pd


def validate_standings(
    dataframe: pd.DataFrame,
):

    if dataframe["participant_id"].isnull().any():
        raise ValueError(
            "Participant ID contains null values."
        )

    if dataframe["points"].isnull().any():
        raise ValueError(
            "Points contains null values."
        )

    if (dataframe["points"] < 0).any():
        raise ValueError(
            "Negative points found."
        )

    if (dataframe["position"] <= 0).any():
        raise ValueError(
            "Invalid position found."
        )

    return True