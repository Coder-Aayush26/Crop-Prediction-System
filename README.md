# 🌱 Crop Prediction System

A Machine Learning web application that predicts the most suitable crop to grow based on soil nutrients and environmental conditions.

This project combines **Machine Learning** and **Flask Web Development** to create an interactive system where users can input soil and weather parameters and receive a crop recommendation.

---

## 🚀 Features

* Predicts the most suitable crop based on soil and environmental data
* User-friendly web interface
* Real-time predictions using a trained machine learning model
* Loading spinner for better user experience
* Clean and responsive UI

---

## 🧠 Machine Learning Model

The model was trained using soil and climate features such as:

* Nitrogen
* Phosphorous
* Potassium
* Temperature
* Humidity
* pH Level
* Rainfall

The trained model is saved using **Pickle** and loaded into the Flask application for predictions.

---

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Scikit-learn**
* **NumPy**
* **HTML**
* **CSS**
* **JavaScript**

---

## 📂 Project Structure

```
Crop-Prediction-System/
│
├── app.py
├── model.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── farmland.jpg
│
└── README.md
```

---

## ⚙️ How to Run the Project

1️⃣ Clone the repository

```
git clone https://github.com/yourusername/Crop-Prediction-System.git
```

2️⃣ Navigate to the project folder

```
cd Crop-Prediction-System
```

3️⃣ Install required dependencies

```
pip install -r requirements.txt
```

4️⃣ Run the Flask application

```
python app.py
```

5️⃣ Open your browser and go to

```
http://127.0.0.1:5000
```

---

## 📊 Input Parameters

Users provide the following inputs:

| Parameter   | Description                 |
| ----------- | --------------------------- |
| Nitrogen    | Nitrogen content in soil    |
| Phosphorous | Phosphorous content in soil |
| Potassium   | Potassium content in soil   |
| Temperature | Temperature in °C           |
| Humidity    | Relative humidity           |
| pH          | Soil pH value               |
| Rainfall    | Rainfall in mm              |

---

## 📌 Future Improvements

* Deploy the application online
* Add more crop datasets
* Improve UI/UX
* Add data visualization
* Allow users to upload soil reports

---

## 👨‍💻 Author

**Aayush**

Machine Learning and Web Development Enthusiast

---

⭐ If you like this project, consider giving it a star on GitHub!
