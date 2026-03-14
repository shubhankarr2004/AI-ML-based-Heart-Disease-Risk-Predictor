# ❤️ Heart Disease Risk Predictor

An interactive web-based **Heart Disease Risk Prediction system** powered by **Machine Learning (Logistic Regression)** and deployed through a **Flask web application**.  
The system predicts whether a person is at risk of developing heart disease based on demographic, lifestyle, and clinical indicators.

---

## ✨ Features

- 🧠 Machine Learning model trained using **Logistic Regression**
- 📊 Risk prediction based on **9 health indicators**
- ⚙️ Feature scaling using **StandardScaler**
- 🌐 Web interface built with **Flask + HTML + CSS + JavaScript**
- 🔄 Real-time predictions via **Flask API endpoint**
- 📉 Displays **risk probability and classification (High Risk / Low Risk)**
- 🧪 Model validated using **cross-validation**
- 📦 Serialized ML model using **Joblib**

---

## 🗂️ Project Structure

```
.
├── model/                          # Saved machine learning artifacts
│   ├── heart_disease_risk_model.pkl
│   └── heart_disease_scaler.pkl
│
├── templates/
│   └── index.html                  # Frontend HTML form
│
├── static/
│   ├── style.css                   # Styling for UI
│   └── script.js                   # JavaScript for API communication
│
├── app.py                          # Flask backend (API + model inference)
└── README.md                       # Project documentation
```

---

## ⚡ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shubhankarr2004/heart-disease-risk-predictor
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv

# Activate environment
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows

pip install -r requirements.txt

```




### 3. Ensure Model Files Are Present

The trained machine learning artifacts must be placed inside the `model/` folder:

```
model/
   heart_disease_risk_model.pkl
   heart_disease_scaler.pkl
```

These files contain the trained Logistic Regression model and the feature scaler used during training.

---

### 4. Run the Flask Server

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5000
```

---

### 5. Use the Web Application

1. Open your browser and go to:

```
http://127.0.0.1:5000
```

2. Enter health information such as:

- Age  
- Gender  
- Blood Pressure  
- Blood Sugar  
- BMI  
- Smoking status  
- Alcohol consumption  
- Urban/Rural residence  

3. Click **Predict Risk**

4. The system will display:

- **Risk Status**
- **Probability of heart disease**

---

## 🖼️ Demo Preview

Example Output:

```
Risk Status: Low Risk
Probability: 7.29%
```

The system calculates the probability using the trained ML model and displays the result dynamically.

---

## 🚀 Future Improvements

- 📊 Add **risk visualization (progress bars/charts)**
- 🧪 Add **input validation for medical ranges**
- 🌐 Deploy online using **Render / Railway / Docker**
- 📈 Provide **feature importance explanations**
- 🧠 Experiment with advanced models like **XGBoost**

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use and modify.

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you’d like to change.

---

## 👨‍💻 Author

Developed by **Shubhankar Singh** ✨  

**LinkedIn:**  
https://www.linkedin.com/in/shubhankarr

**GitHub:**  
https://github.com/shubhankarr2004
