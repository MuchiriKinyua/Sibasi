from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.neighbors import NearestNeighbors

# Load saved model and matrix
knn_model = joblib.load('knn_model.pkl')
user_item = joblib.load('user_item_matrix.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None

    if request.method == 'POST':
        customer_id = int(request.form['customer_id'])

        if customer_id in user_item.index:
            # Get vector for this customer
            customer_vector = user_item.loc[customer_id].values.reshape(1, -1)

            # Find similar customers
            distances, indices = knn_model.kneighbors(customer_vector, n_neighbors=6)
            similar_indices = indices.flatten()[1:]  # exclude self
            similar_customers = user_item.index[similar_indices]

            # Compute weighted product scores
            weighted_scores = np.zeros(user_item.shape[1])
            for idx, sim_cust in enumerate(similar_customers):
                weighted_scores += user_item.loc[sim_cust].values * (1 - distances.flatten()[idx + 1])  # closer = higher weight

            # Filter out already bought
            already_bought = user_item.loc[customer_id]
            weighted_scores[already_bought > 0] = 0

            # Recommend top products
            product_indices = weighted_scores.argsort()[::-1][:5]
            recommendations = user_item.columns[product_indices].tolist()
        else:
            recommendations = ["Customer ID not found."]

    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
