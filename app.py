from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    nitrogen = float(request.form["Nitrogen"])
    phosphorous = float(request.form["Phosphorous"])
    potassium = float(request.form["Potassium"])
    temperature = float(request.form["Temperature"])
    humidity = float(request.form["Humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["Rainfall"])

    features = np.array([[nitrogen, phosphorous, potassium,
                          temperature, humidity, ph, rainfall]])
    import time
    time.sleep(3)
    prediction = model.predict(features)

    return render_template("index.html",
                           prediction_text=f"Recommended Crop: {prediction[0]}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)