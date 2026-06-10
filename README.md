# 🎬 Movie Recommendation System

## 📌 Overview

The Movie Recommendation System is a Machine Learning project that provides personalized movie recommendations using a Hybrid Recommendation Approach combining:

- Content-Based Filtering
- Collaborative Filtering (SVD)
- Popularity-Based Ranking

The system is built using the MovieLens 32M Dataset and deployed as an interactive Streamlit web application.

---

## 🚀 Live Demo

🔗 [(https://movie-recommendation-system-8uwrnuzuoy2gybgcmgc2dx.streamlit.app/)]

---

## 📂 Images
<img width="1920" height="1080" alt="Screenshot (417)" src="https://github.com/user-attachments/assets/265e3d9e-7b14-4de6-adde-fdf58f850f7d" />
<img width="1920" height="1080" alt="Screenshot (418)" src="https://github.com/user-attachments/assets/2d0957ae-8017-40ed-bc8c-26b117afee54" />
<img width="1920" height="1080" alt="Screenshot (419)" src="https://github.com/user-attachments/assets/4ac07752-9870-46b8-9b52-9545485a4f26" />
<img width="1920" height="1080" alt="Screenshot (420)" src="https://github.com/user-attachments/assets/e1ea8e01-7a03-4896-b70a-520bf8d7d051" />
<img width="1920" height="1080" alt="Screenshot (422)" src="https://github.com/user-attachments/assets/9fa7cae2-1316-4f12-86ce-15fcf78c75c5" />
<img width="1920" height="1080" alt="Screenshot (421)" src="https://github.com/user-attachments/assets/8f41567f-ee5c-4d38-bc01-253d77d83af5" />




---

## 🎯 Problem Statement

With thousands of movies available on streaming platforms, users often struggle to find movies that match their interests.

This project solves this problem by building an intelligent recommendation system capable of:

- Recommending similar movies
- Predicting user preferences
- Generating personalized recommendations
- Combining multiple recommendation techniques

---

## 📊 Dataset

### MovieLens 32M Dataset

| Metric | Value |
|----------|----------|
| Ratings | 32 Million |
| Tags | 2 Million |
| Movies | 87,585 |
| Users | 200,948 |

### Dataset Files

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

Dataset Source:

https://grouplens.org/datasets/movielens/

---

## 🏗️ Project Architecture

```text
MovieLens Dataset
       │
       ▼
Data Collection
       │
       ▼
Data Preprocessing
       │
       ▼
Exploratory Data Analysis
       │
       ▼
Feature Engineering
       │
       ▼
Content-Based Filtering
       │
       ▼
Collaborative Filtering (SVD)
       │
       ▼
Hybrid Recommendation System
       │
       ▼
Streamlit Web Application
```

---

## ⚙️ Technologies Used

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-Learn
- Scikit-Surprise

### Visualization

- Matplotlib
- Seaborn
- Plotly

### Deployment

- Streamlit
- Hugging Face Hub

### APIs

- TMDB API

### Version Control

- Git
- GitHub

---

# 📋 Project Workflow

## 1️⃣ Data Collection

Collected MovieLens 32M Dataset.

Files Used:

- movies.csv
- ratings.csv
- tags.csv
- links.csv

---

## 2️⃣ Data Preprocessing

Performed:

- Missing Value Analysis
- Duplicate Removal
- Data Type Conversion
- Dataset Merging
- Feature Cleaning

### Missing Values

#### tags.csv

| Column | Missing Values |
|----------|----------|
| tag | 17 |

#### links.csv

| Column | Missing Values |
|----------|----------|
| tmdbId | 124 |

---

## 3️⃣ Exploratory Data Analysis (EDA)

Performed:

- Ratings Distribution Analysis
- Most Rated Movies
- Highest Rated Movies
- Genre Distribution
- User Activity Analysis
- Movie Popularity Analysis

### Visualizations

- Histograms
- Bar Charts
- Pie Charts
- Scatter Plots
- Heatmaps

---

## 4️⃣ Feature Engineering

Created:

- Average Rating
- Rating Count
- Popularity Score
- Normalized Popularity Score

These features improve recommendation quality.

---

# 🎥 Content-Based Filtering

## Objective

Recommend movies similar to the selected movie.

## Methodology

1. Combine genres and tags.
2. Apply TF-IDF Vectorization.
3. Create movie feature vectors.
4. Calculate Cosine Similarity.

### Libraries Used

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
```

### Example

```text
Input:
Toy Story (1995)

Output:
Top Similar Movies
```

---

# 🤝 Collaborative Filtering

## Objective

Recommend movies based on user behavior.

## Methodology

Used Singular Value Decomposition (SVD).

### Steps

1. Build User-Movie Matrix
2. Train SVD Model
3. Learn Latent Features
4. Predict Ratings for Unseen Movies

### Library

```python
from surprise import SVD
```

### Example

```python
svd_model.predict(
    user_id,
    movie_id
)
```

---

# 🔥 Hybrid Recommendation System

The final recommendation combines:

```text
Content Similarity
+
Collaborative Filtering
+
Popularity Score
```

### Formula

```python
Hybrid Score = (
    0.5 * Collaborative_Score
    +
    0.3 * Content_Score
    +
    0.2 * Popularity_Score
)
```

### Advantages

- Better Personalization
- Higher Accuracy
- Reduced Cold Start Problem
- Improved Recommendation Diversity

---

# 📈 Model Evaluation

| Metric | Value |
|----------|----------|
| RMSE | 0.8814 |
| MAE | 0.6717 |
| Precision@10 | 0.4329 |
| Recall@10 | 0.3266 |
| F1 Score | 0.3723 |
| Coverage (%) | 9.31 |

### Interpretation

- Lower RMSE indicates better rating prediction.
- Precision@10 measures recommendation relevance.
- Recall@10 measures recommendation coverage.
- F1 Score balances Precision and Recall.

---

# 💾 Saved Model Files

```text
saved_models/
│
├── movies.pkl
├── links.pkl
├── movie_indices.pkl
├── tfidf_matrix.pkl
├── svd_model.pkl
```

### movies.pkl

Stores movie metadata.

### links.pkl

Stores MovieLens to TMDB mapping.

### movie_indices.pkl

Stores movie title to index mapping.

### tfidf_matrix.pkl

Stores TF-IDF vectors for content similarity.

### svd_model.pkl

Stores trained collaborative filtering model.

---

# 🌐 TMDB API Integration

Features:

- Movie Posters
- Movie Overview
- Ratings
- Release Date
- Movie Trailers

### Workflow

```text
MovieLens ID
      │
      ▼
TMDB ID
      │
      ▼
TMDB API
      │
      ▼
Movie Details & Trailer
```

---

# 🖥️ Streamlit Application Features

✅ Movie Search

✅ Content-Based Recommendations

✅ Collaborative Filtering

✅ Hybrid Recommendations

✅ Movie Posters

✅ Movie Details

✅ Movie Trailers

✅ Interactive Dashboard

---

# 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── download_models.py
├── Dockerfile
├── requirements.txt
├── README.md
│
├── assets/
│
├── data/
│
├── utils/
│   ├── recommender.py
│   └── tmdb_helper.py
│
└── saved_models/
    ├── movies.pkl
    ├── links.pkl
    ├── movie_indices.pkl
    ├── tfidf_matrix.pkl
    └── svd_model.pkl
```

---

# 🚀 Deployment

### Training Environment

- Google Colab

### Deployment Platform

- Streamlit

### Model Hosting

- Hugging Face Hub

### Deployment Workflow

```text
Google Colab
      │
      ▼
Train Models
      │
      ▼
Save .pkl Files
      │
      ▼
Upload to Hugging Face Hub
      │
      ▼
Streamlit Application
      │
      ▼
Live Deployment
```

---

# 🧩 Challenges Faced

- Processing MovieLens 32M Dataset
- Sparse User-Movie Matrix
- Large Model Storage
- Memory Optimization
- Hugging Face Deployment
- Streamlit Deployment
- Docker Compatibility
- Large File Downloads

---

# 🎯 Key Learnings

- Recommendation Systems
- Content-Based Filtering
- Collaborative Filtering
- Hybrid Recommendation Systems
- Machine Learning Pipelines
- Feature Engineering
- Model Evaluation
- Streamlit Deployment
- Hugging Face Model Hosting

---

# 👨‍💻 Author

**Kushvanth Venkata Karthik**

Aspiring Data Scientist | Machine Learning Engineer | Full Stack Developer

### Connect With Me

- LinkedIn: [https://www.linkedin.com/in/kushvanth-badisa/]
- GitHub: [https://github.com/Kushvanth015/Kushvanth015/blob/main/README.md]

---

⭐ If you found this project useful, please give it a star!
