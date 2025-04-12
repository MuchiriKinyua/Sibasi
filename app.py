import streamlit as st
import pandas as pd
import pyodbc
from sklearn.metrics.pairwise import cosine_similarity

# --- Database Connection ---
@st.cache_resource
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=AdventureWorks2022;'
        'UID=SA;'
        'PWD=Sarahwanjiru77@'
    )

# --- Load Data ---
@st.cache_data
def load_data():
    conn = get_connection()
    query = """
        SELECT soh.CustomerID, sod.ProductID, COUNT(*) as OrderCount
        FROM Sales.SalesOrderHeader soh
        JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
        WHERE soh.CustomerID IS NOT NULL
        GROUP BY soh.CustomerID, sod.ProductID;
    """
    df = pd.read_sql(query, conn)
    return df

# --- Prepare Recommendation Matrix ---
def prepare_matrix(data):
    user_item = data.pivot_table(index='CustomerID', columns='ProductID', values='OrderCount', fill_value=0)
    similarity_df = pd.DataFrame(cosine_similarity(user_item), index=user_item.index, columns=user_item.index)
    return user_item, similarity_df

# --- Recommendation Logic ---
def recommend_products(customer_id, user_item, similarity_df, top_n=5):
    if customer_id not in user_item.index:
        return f"Customer ID {customer_id} not found."

    similar_customers = similarity_df[customer_id].sort_values(ascending=False)[1:6]  # Top 5 excluding self

    weighted_scores = pd.Series(0, index=user_item.columns)
    for sim_cust, score in similar_customers.items():
        weighted_scores += user_item.loc[sim_cust] * score

    already_bought = user_item.loc[customer_id][user_item.loc[customer_id] > 0].index
    recommendations = weighted_scores.drop(index=already_bought)

    return recommendations.sort_values(ascending=False).head(top_n)

# --- Streamlit UI ---
st.title("🎯 Customer Product Recommendation - Adventure Works")

df = load_data()
user_item_matrix, sim_matrix = prepare_matrix(df)

all_customers = sorted(user_item_matrix.index.tolist())
selected_customer = st.selectbox("Select Customer ID:", all_customers)

if st.button("Get Recommendations"):
    recs = recommend_products(selected_customer, user_item_matrix, sim_matrix)
    st.subheader(f"📦 Top Recommendations for Customer {selected_customer}:")
    st.table(recs.reset_index().rename(columns={0: "Score"}))
