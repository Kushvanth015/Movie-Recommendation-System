import pickle
import pandas as pd

from sklearn.metrics.pairwise import linear_kernel

# Load models:

print("Loading movies.pkl...")
movies = pd.read_pickle(
    "movies.pkl"
)
print("✅ movies.pkl loaded")

print("Loading links.pkl...")
links = pd.read_pickle(
    "links.pkl"
)
print("✅ links.pkl loaded")

print("Loading svd_model.pkl...")
with open(
    "svd_model.pkl",
    "rb"
) as f:
    svd_model = pickle.load(f)
print("✅ svd_model.pkl loaded")

print("Loading tfidf_matrix.pkl...")
with open(
    "tfidf_matrix.pkl",
    "rb"
) as f:
    tfidf_matrix = pickle.load(f)
print("✅ tfidf_matrix.pkl loaded")

print("Loading movie_indices.pkl...")
with open(
    "movie_indices.pkl",
    "rb"
) as f:
    movie_indices = pickle.load(f)
print("✅ movie_indices.pkl loaded")

# Content Recommendation

def content_recommendations(
        movie_title,
        top_n=10):

    if movie_title not in movie_indices.index:

        return None

    idx = movie_indices[movie_title]

    similarities = linear_kernel(
        tfidf_matrix[idx:idx+1],
        tfidf_matrix
    ).flatten()

    indices = similarities.argsort(
    )[::-1][1:top_n+1]

    return movies.iloc[
        indices
    ]

# Collaborative Recommendation

def predict_rating(
        user_id,
        movie_id):

    return svd_model.predict(
        user_id,
        movie_id
    ).est
    
# Hybrid Recommendation

def hybrid_recommendations(
        user_id,
        movie_title,
        top_n=10):

    idx = movie_indices[movie_title]

    similarities = linear_kernel(
        tfidf_matrix[idx:idx+1],
        tfidf_matrix
    ).flatten()

    candidate_indices = (
        similarities
        .argsort()[::-1]
        [1:1001]
    )

    results = []

    for i in candidate_indices:

        movie_id = movies.iloc[i][
            "movieId"
        ]

        content_score = similarities[i]

        collaborative_score = (
            svd_model.predict(
                user_id,
                movie_id
            ).est
        )

        popularity_score = (
            movies.iloc[i][
                "popularity_norm"
            ]
        )

        hybrid_score = (

            0.5 *
            collaborative_score

            +

            0.3 *
            content_score

            +

            0.2 *
            popularity_score

        )

        results.append(
            (
                i,
                hybrid_score
            )
        )

    results = sorted(
        results,
        key=lambda x: x[1],
        reverse=True
    )

    top_indices = [
        x[0]
        for x in results[:top_n]
    ]

    return movies.iloc[
        top_indices
    ]

print("STEP 2: Loading movies.pkl")
print("STEP 3: Loading links.pkl")
print("STEP 4: Loading svd_model.pkl")
print("STEP 5: Loading tfidf_matrix.pkl")
print("STEP 6: Loading movie_indices.pkl")