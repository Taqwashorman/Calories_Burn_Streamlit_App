# 🔥 Calories Burned Prediction App

## 🚀 Try the App

You can try the live app here:  
👉 [Calories Burned App](https://caloriesburnappapp-ctc9fe7gx9d9dicp8sq65o.streamlit.app/)

## About the Project
This is a simple Streamlit web application that predicts the number of calories burned during exercise based on user input, such as:

- Age
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature
- Gender

## 💡 How it Works

The model behind this app is trained using **XGBoost**, and the prediction is made based on a regression model that takes physiological and exercise-related data as input.

The app is built using:

- Streamlit
- NumPy
- Joblib
- XGBoost

## 📦 Installation (Optional for local use)

To run the app locally:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
