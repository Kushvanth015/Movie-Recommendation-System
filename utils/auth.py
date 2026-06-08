import pandas as pd
import hashlib
import os

USERS_FILE = "data/users.csv"


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def register_user(
        username,
        email,
        password):

    if not os.path.exists(
            USERS_FILE):
        pd.DataFrame(
            columns=[
                "username",
                "email",
                "password"
            ]
        ).to_csv(
            USERS_FILE,
            index=False
        )

    users = pd.read_csv(
        USERS_FILE
    )

    if username in users[
        "username"
    ].values:
        return False

    users.loc[len(users)] = [
        username,
        email,
        hash_password(
            password
        )
    ]

    users.to_csv(
        USERS_FILE,
        index=False
    )

    return True


def login_user(
        username,
        password):

    users = pd.read_csv(
        USERS_FILE
    )

    hashed = hash_password(
        password
    )

    match = users[
        (
            users["username"]
            ==
            username
        )
        &
        (
            users["password"]
            ==
            hashed
        )
    ]

    return len(match) > 0