import os
import requests

FILES = {
    "movies.pkl": "https://huggingface.co/Kushvanth05/movie-recommendation-models/resolve/main/saved_models/movies.pkl",
    "links.pkl": "https://huggingface.co/Kushvanth05/movie-recommendation-models/resolve/main/saved_models/links.pkl",
    "svd_model.pkl": "https://huggingface.co/Kushvanth05/movie-recommendation-models/resolve/main/saved_models/svd_model.pkl",
    "tfidf_matrix.pkl": "https://huggingface.co/Kushvanth05/movie-recommendation-models/resolve/main/saved_models/tfidf_matrix.pkl",
    "movie_indices.pkl": "https://huggingface.co/Kushvanth05/movie-recommendation-models/resolve/main/saved_models/movie_indices.pkl",
}

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        r = requests.get(url, stream=True)
        r.raise_for_status()

        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded {filename}")

def download_models():
    for filename, url in FILES.items():
        download_file(url, filename)