# Product Recommendation System

![Screenshot from 2025-04-13 05-11-01](https://github.com/user-attachments/assets/dc550d33-6170-4257-b7b6-5b31e20b4dcc)

A customer-product recommender system built using collaborative filtering (User-Based, Item-Based, and KNN-based), following the CRISP-DM methodology. It allows users to input a CustomerID and receive product recommendations via a Flask web interface.

# Project Overview

This project demonstrates how to build and deploy a recommendation system using customer order data. The core algorithm uses K-Nearest Neighbors (KNN) collaborative filtering to predict product interest based on similarity.

# CRISP-DM Process
1. Business Understanding

I aim to build a system that can recommend products to customers based on their purchase history and similarities to other customers. This can increase cross-sells and customer satisfaction.
2. Data Understanding

I worked with a dataset containing:

    CustomerID

    ProductID

    OrderQty

Exploratory analysis included:

    Heatmaps of Customer vs Product interactions

    Purchase behavior insights

3. Data Preparation

Performed:

    Feature engineering

    Created a user-item interaction matrix

    Converted data into a format suitable for collaborative filtering

4. Modeling

Implemented:

    User-Based Collaborative Filtering

    Item-Based Collaborative Filtering

    KNN-based Collaborative Filtering using sklearn.neighbors.NearestNeighbors

    Saved trained model with joblib

5. Evaluation

Recommendations were tested using manual inspection of outputs for various customers. Future improvements can include recall/precision metrics or A/B testing.

6. Deployment

A Flask web app was created for easy interaction:

    Users enter a CustomerID

    Recommended ProductIDs are returned

    Simple and clean UI using HTML & CSS

# Local Deployment Instructions
1. Clone the Repo

git clone https://github.com/MuchiriKinyua/Customer-Recommendation-System

2. Create and Activate a Virtual Environment

python3 -m venv myenv
source myenv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Flask App

python app.py

Visit http://127.0.0.1:5000/ in your browser to use the app.
Project Structure

project/ </br>
│
├── app.py                      # Flask web app </br>
├── knn_model.pkl               # Saved KNN model </br>
├── user_item_matrix.pkl        # Saved user-item matrix </br>
├── main.ipynb                  # Full CRISP-DM modeling notebook </br>
├── template/ </br>
│   └── index.html              # Frontend HTML form </br>
└── README.md                   # Project documentation

# Future Work

    Add more ML models (SVD, Matrix Factorization)

    Evaluate using precision/recall

    Incorporate product metadata and categories

    Deploy on cloud platforms (Heroku, Render, or AWS)

# Built With

    Python

    Pandas, Scikit-learn, Joblib

    Flask

    HTML/CSS
