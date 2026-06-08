import streamlit as st
import pandas as pd
import plotly.express as px

from download_models import download_models
download_models()

from utils.auth import (
    login_user,
    register_user
)

from utils.recommender import (
    movies,
    links,
    content_recommendations,
    hybrid_recommendations
)

from utils.tmdb_helper import (
    get_movie_details,
    get_trailer
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------------
# LOGIN / REGISTER PAGE
# -----------------------------------

if not st.session_state.logged_in:

    st.title("🎬 Movie Recommendation System")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Register"]
    )

    # REGISTER

    if menu == "Register":

        st.subheader("Create Account")

        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Register"):

            if register_user(
                username,
                email,
                password
            ):

                st.success(
                    "Registration successful. Please login."
                )

            else:

                st.error(
                    "Username already exists."
                )

    # LOGIN

    elif menu == "Login":

        st.subheader("Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if login_user(
                username,
                password
            ):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

    st.stop()
    
st.sidebar.success(
    f"Welcome {st.session_state.username}"
)

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    if "username" in st.session_state:
        del st.session_state["username"]

    st.rerun()

# Your Movie Recommendation UI here

# -----------------------------------
# THEME
# -----------------------------------

theme = st.sidebar.radio(
    "Theme",
    ["Light", "Dark"]
)

if theme == "Dark":

    st.markdown(
        """
        <style>
        .stApp{
            background-color:#0e1117;
            color:white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🎬 AI Movie Recommendation System")

# -----------------------------------
# SIDEBAR
# -----------------------------------

user_id = st.sidebar.number_input(
    "User ID",
    min_value=1,
    value=100
)

recommendation_type = st.sidebar.selectbox(
    "Recommendation Type",
    [
        "Content-Based",
        "Hybrid"
    ]
)

# -----------------------------------
# TRENDING MOVIES
# -----------------------------------

st.sidebar.header("🔥 Trending Movies")

if "rating_count" in movies.columns:

    trending_movies = (
        movies
        .sort_values(
            "rating_count",
            ascending=False
        )
        .head(10)
    )

    for movie in trending_movies["title"]:

        st.sidebar.write(movie)

# -----------------------------------
# GENRE FILTER
# -----------------------------------

all_genres = sorted(
    set(
        genre
        for genres in movies["genres"].dropna()
        for genre in genres.split("|")
    )
)

selected_genres = st.multiselect(
    "Filter by Genre",
    all_genres
)

filtered_movies = movies.copy()

if selected_genres:

    filtered_movies = filtered_movies[
        filtered_movies["genres"].apply(
            lambda x:
            any(
                g in str(x)
                for g in selected_genres
            )
        )
    ]

# -----------------------------------
# MOVIE SEARCH
# -----------------------------------

movie_name = st.selectbox(
    "Select a Movie",
    sorted(
        filtered_movies["title"]
        .unique()
    )
)

# -----------------------------------
# RECENTLY VIEWED
# -----------------------------------

if "recent_movies" not in st.session_state:

    st.session_state.recent_movies = []

if movie_name not in st.session_state.recent_movies:

    st.session_state.recent_movies.insert(
        0,
        movie_name
    )

st.sidebar.header("🕒 Recently Viewed")

for movie in st.session_state.recent_movies[:10]:

    st.sidebar.write(movie)

# -----------------------------------
# RECOMMEND BUTTON
# -----------------------------------

if st.button("Recommend Movies"):

    if recommendation_type == "Content-Based":

        recs = content_recommendations(
            movie_name,
            top_n=10
        )

    else:

        recs = hybrid_recommendations(
            user_id,
            movie_name,
            top_n=10
        )

    st.subheader(
        "🎯 Recommended Movies"
    )

    for _, row in recs.iterrows():

        movie_id = row["movieId"]

        details = None

        tmdb_row = links[
            links["movieId"]
            ==
            movie_id
        ]

        if not tmdb_row.empty:

            tmdb_id = (
                tmdb_row["tmdbId"]
                .values[0]
            )

            if pd.notna(tmdb_id):

                details = get_movie_details(
                    tmdb_id
                )

        col1, col2 = st.columns(
            [1, 3]
        )

        # --------------------------
        # POSTER
        # --------------------------

        with col1:

            if details and details.get(
                "poster"
            ):

                st.image(
                    details["poster"],
                    width=180
                )

            else:

                st.image(
                    "https://via.placeholder.com/180x270?text=No+Poster",
                    width=180
                )

        # --------------------------
        # MOVIE DETAILS
        # --------------------------

        with col2:

            st.subheader(
                row["title"]
            )

            st.write(
                f"🎭 Genres: {row['genres']}"
            )

            if "avg_rating" in row.index:

                st.write(
                    f"⭐ Average Rating: {row['avg_rating']:.2f}"
                )

            if details:

                st.write(
                    f"📅 Release Date: {details.get('release_date','N/A')}"
                )

                st.write(
                    f"🎬 TMDB Rating: {details.get('vote_average','N/A')}"
                )

                st.write(
                    details.get(
                        "overview",
                        "No overview available."
                    )
                )

                trailer_url = get_trailer(
                    tmdb_id
                )

                if trailer_url:

                    st.video(
                        trailer_url
                    )

        st.divider()

    # -----------------------------------
    # EXPLANATION
    # -----------------------------------

    st.info(
        f"""
        Recommended because:

        • Similar to **{movie_name}**

        • High predicted rating

        • Popular among users

        • Strong hybrid recommendation score
        """
    )

# -----------------------------------
# MODEL PERFORMANCE
# -----------------------------------

st.header("📊 Model Performance")

col1, col2, col3 = st.columns(3)

col1.metric(
    "RMSE",
    "0.8814"
)

col2.metric(
    "MAE",
    "0.6717"
)

col3.metric(
    "Precision@10",
    "0.4329"
)

metrics_df = pd.DataFrame({

    "Metric": [
        "RMSE",
        "MAE",
        "Precision",
        "Recall",
        "F1 Score",
        "Coverage"
    ],

    "Value": [
        0.8814,
        0.6717,
        0.4329,
        0.3266,
        0.3723,
        9.31
    ]
})

fig = px.bar(
    metrics_df,
    x="Metric",
    y="Value",
    title="Recommendation Model Metrics"
)

st.plotly_chart(
    fig,
    use_container_width=True
)