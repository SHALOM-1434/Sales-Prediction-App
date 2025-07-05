# Rossmann Sales Forecast App

A machine learning-powered web application built with **Flask** and **XGBoost** that predicts daily sales for retail stores based on historical patterns and store-specific features.

---

## Project Overview

The goal of this project is to help business managers and analysts make **data-driven decisions** using a predictive model trained on the **Rossmann Store Sales dataset**. It forecasts sales for a given store and date, helping optimize planning, staffing, and inventory.

---

## Features

- Predicts daily sales based on store-specific inputs
- Built using a trained **XGBoost Regression model**
- Interactive web interface with **Flask**
- Feature engineering and hyperparameter tuning for improved accuracy
- Easy deployment (e.g., Render, Replit, or local)

---

## Tech Stack

| Task                    | Tool/Library         |
|-------------------------|----------------------|
| Model Training          | XGBoost, Scikit-learn|
| Data Analysis & Cleaning| Pandas, NumPy        |
| Visualization           | Matplotlib, Seaborn  |
| Web Framework           | Flask                |

---

## Dataset

- Source: Rossmann Store Sales dataset
- Includes features like promotions, holidays, store types, and competition

---

## Model Performance

| Metric | Value |
|--------|-------|
| R²     | 0.949 |
| RMSE   | ~701  |
| MAE    | ~480  |

*Model was tuned using `GridSearchCV` for improved performance.*

---

## Project Structure

- `app.py` — Flask application
- `xgb_sales_model.pkl` — Trained XGBoost model
- `templates/` — Contains `index.html` and `result.html` for web interface
- `requirements.txt` — Python dependencies

---

## How to Use the App

1. **Clone the repository** or download the files
2. *(Optional)* Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
 3. *Install dependencies*: pip install -r requirements.txt
 4. *Run the Flask app*: python app.py
 5. *Open your browser and go to*: http://127.0.0.1:5000

---

## Screenshots of App Form and Prediction Page
![Sales Pred  1](https://github.com/user-attachments/assets/0b8b6dfa-95fb-41b6-ba45-3dd826058ffa)
![Sales Pred 2](https://github.com/user-attachments/assets/ef421309-5e6a-4c30-bae1-4569df66f394)
![Sales Pred Result](https://github.com/user-attachments/assets/fef60c43-ada7-474b-a77e-6014a260870b)

---

## Author

Peace Ginika  
Data Analyst & ML Developer  
LinkedIn: https://www.linkedin.com/in/peaceginika/

---

## Live App

Try the live sales prediction app here:  
https://rossmann-sales-prediction-01uw.onrender.com 


## License

This project is open-source and free to use for educational and non-commercial purposes.





