# Customer Recommendation System

![Screenshot from 2025-04-12 14-21-01](https://github.com/user-attachments/assets/756b3d10-b453-46cb-8fb5-756a5a882fb6)

This Streamlit app provides personalized **product recommendations** for customers based on their purchase history from the **AdventureWorks2022** SQL Server database.

## Features

- Fetches live data from AdventureWorks SQL Server database
- Uses collaborative filtering via cosine similarity
- Recommends top products for each customer
- Simple UI using Streamlit for ease of use


## Prerequisites

### SQL Server
Make sure your **AdventureWorks2022** database is running and accessible.

## Setup

1. **Clone the project**
   ```bash
   git clone https://github.com/MuchiriKinyua/Sibasi

then

   cd Sibasi

Create a virtual environment

python -m venv myenv
source myenv/bin/activate

Install dependencies

pip install -r requirements.txt

Run the app

    streamlit run app.py

Database Connection

Make sure your SQL Server is running and accepting connections. The app uses the following connection string:

pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost,1433;'
    'DATABASE=AdventureWorks2022;'
    'UID=SA;'
    'PWD=yourStrong(!)Password'
)


# How it Works

    Pulls customer-product order data

    Builds a user-product matrix

    Computes cosine similarity between customers

    Recommends products not yet purchased by the customer but favored by similar ones

# Dependencies

    streamlit

    pandas

    pyodbc

    scikit-learn

Install them with:

pip install streamlit pandas pyodbc scikit-learn
