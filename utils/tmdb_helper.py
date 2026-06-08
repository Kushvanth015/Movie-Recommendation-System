import requests
import streamlit as st

TMDB_API_KEY = "a14956f3d4829005ab4f101b61120021"


def get_movie_details(tmdb_id):

    try:

        url = (
            f"https://api.themoviedb.org/3/movie/"
            f"{int(tmdb_id)}"
            f"?api_key={TMDB_API_KEY}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        poster = None

        if data.get("poster_path"):

            poster = (
                "https://image.tmdb.org/t/p/w500"
                + data["poster_path"]
            )

        return {
            "poster": poster,
            "overview": data.get("overview"),
            "release_date": data.get("release_date"),
            "vote_average": data.get("vote_average")
        }

    except Exception:
        return None


def get_trailer(tmdb_id):

    try:

        url = (
            f"https://api.themoviedb.org/3/movie/"
            f"{int(tmdb_id)}"
            f"/videos"
            f"?api_key={TMDB_API_KEY}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        videos = data.get("results", [])

        for video in videos:

            if (
                video.get("site") == "YouTube"
                and
                video.get("type") == "Trailer"
            ):

                return (
                    "https://www.youtube.com/watch?v="
                    + video["key"]
                )

        return None

    except Exception:
        return None