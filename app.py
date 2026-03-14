from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model/heart_disease_risk_model.pkl")
scaler = joblib.load("model/heart_disease_scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = np.array([[
        float(data["age"]),
        int(data["gender"]),
        float(data["systolic_bp"]),
        float(data["diastolic_bp"]),
        float(data["blood_sugar"]),
        float(data["bmi"]),
        int(data["smoking"]),
        int(data["alcohol"]),
        int(data["urban"])
    ]])

    scaled_input = scaler.transform(input_data)
    probability = model.predict_proba(scaled_input)[0][1]

    prediction = "High Risk" if probability >= 0.5 else "Low Risk"

    return jsonify({
        "risk_probability": round(probability * 100, 2),
        "risk_label": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)