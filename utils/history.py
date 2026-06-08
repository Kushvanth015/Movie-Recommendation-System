import pandas as pd
from datetime import datetime

FILE = "data/history.csv"


def save_history(
        username,
        movie_title,
        rec_type):

    df = pd.read_csv(FILE)

    new_row = pd.DataFrame({

        "username":
        [username],

        "movie_title":
        [movie_title],

        "recommendation_type":
        [rec_type],

        "timestamp":
        [datetime.now()]

    })

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        FILE,
        index=False
    )


def get_history(
        username):

    df = pd.read_csv(FILE)

    return df[
        df["username"]
        ==
        username
    ]