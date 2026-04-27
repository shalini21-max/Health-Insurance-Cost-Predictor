# 🏥 Health Insurance Cost Predictor

## 📌 Overview

This project predicts the medical insurance cost of an individual based on various features such as age, BMI, smoking habits, number of children, and region using Machine Learning algorithms.

The main objective is to help insurance companies and individuals estimate expected medical expenses accurately.

---

## 🚀 Features

* Predict insurance cost based on user input
* Multiple ML model implementation and comparison
* Data preprocessing and feature engineering
* Data visualization for better insights
* Clean and simple user interface

---

## 🧠 Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib / Seaborn
* Scikit-learn
* XGBoost
* Jupyter Notebook

---

## 📊 Dataset

The dataset used contains the following features:

* Age
* Sex
* BMI
* Number of Children
* Smoking Status
* Region
* Charges (Target Variable)

---

## 🖥️ Application Interface

<p align="center">
  <img src="images/ui.png" alt="Health Insurance Cost Predictor UI" width="650"/>
</p>

---

## 📈 Models Used

### 🔹 Linear Regression

* Used as a baseline model
* Helps understand linear relationships between features and target

### 🔹 Ridge Regression

* Applies L2 regularization
* Reduces overfitting and improves model performance

### 🔹 XGBoost Regressor

* Advanced ensemble algorithm based on gradient boosting
* Captures complex and non-linear relationships
* Achieved the best performance among all models

---

## 🏆 Model Performance

Models were evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

👉 XGBoost provided the highest accuracy and lowest error.

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/shalini21-max/Health-Insurance-Cost-Predictor.git
```

2. Navigate to the project directory:

```bash
cd Health-Insurance-Cost-Predictor
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the project using:

```bash
python app.py
```

or open Jupyter Notebook:

```bash
jupyter notebook
```

---

## 📊 Project Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Building
6. Model Evaluation
7. Prediction

---

## 🔮 Future Improvements

* Deploy as a web application (Flask / Streamlit)
* Improve model accuracy with advanced tuning
* Add more real-world features
* Create an interactive dashboard

---

## 👩‍💻 Author

**Shalini Mishra**

* GitHub: https://github.com/shalini21-max

---

## 📄 License

This project is open-source and available under the MIT License.
