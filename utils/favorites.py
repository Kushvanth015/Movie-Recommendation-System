import pandas as pd

FILE = "data/favorites.csv"


def add_favorite(
        username,
        movie_id):

    df = pd.read_csv(FILE)

    new_row = pd.DataFrame({
        "username":
        [username],

        "movieId":
        [movie_id]
    })

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        FILE,
        index=False
    )


def get_favorites(
        username):

    df = pd.read_csv(FILE)

    return df[
        df["username"]
        ==
        username
    ]