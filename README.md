
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
6. *Enter store details and get predicted sales instantly!*

---

## Screenshots of App Form and Prediction Page


![Sales Pred  1](https://github.com/user-attachments/assets/064efd66-0a98-4057-b662-34056b10cd7f)

![Sales Pred 2](https://github.com/user-attachments/assets/d502cdca-307b-4a7f-ba63-5f5dd5ba1283)
![Sales Pred Result](https://github.com/user-attachments/assets/0f1f6952-0640-4b07-aee9-e1651927af04)

## Author

Peace Ginika  
Data Analyst & ML Developer
https://www.linkedin.com/in/peaceginika/   

## License

This project is open-source and free to use for educational and non-commercial purposes.


