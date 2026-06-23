from flask import Flask, request, jsonify
import pickle
import numpy as np
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
app = Flask(__name__)

with open("fraud_model1.pkl", "rb") as f:
    model = pickle.load(f)
@app.route("/")
def home():
    return "Fraud Detection API Running Successfully"
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    required_fields = [
        "Unnamed_0","cc_num","amt","zip","lat","long",
        "city_pop","unix_time","merch_lat","merch_long",
        "hour","day","month"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is missing"
            }), 400

    features = np.array([
        data["Unnamed_0"],
        data["cc_num"],
        data["amt"],
        data["zip"],
        data["lat"],
        data["long"],
        data["city_pop"],
        data["unix_time"],
        data["merch_lat"],
        data["merch_long"],
        data["hour"],
        data["day"],
        data["month"]
    ]).reshape(1,-1)

    prediction = model.predict(features)[0]
    logging.info(
        f"Prediction={prediction}, "
        f"Amount={data['amt']}, "
        f"CC={data['cc_num']}"
    )
    return jsonify({
        "fraud_prediction": int(prediction)
    })

if __name__ == "__main__":
    app.run(debug=True)