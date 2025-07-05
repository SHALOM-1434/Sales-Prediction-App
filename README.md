🧾 SALES FORECASTING FLASK APP PROJECT - README

🔧 Project Structure:
-----------------------
sales_forecast_app/
│
├── app.py                  --> Main Flask application (backend)
├── xgb_sales_model.pkl     --> Trained XGBoost model file
├── requirements.txt        --> List of required libraries (to be created later)
├── templates/
│   ├── index.html          --> Form UI for entering input
│   └── result.html         --> Page that displays predicted sales

🧠 What Each File Does:
-----------------------
- app.py:
  Hosts the web application using Flask, loads the trained model, receives input,
  predicts results, and routes to the appropriate HTML template.

- index.html:
  Frontend form where the user inputs features like Store, Promo, etc.

- result.html:
  Displays the prediction (sales forecast) result.

- xgb_sales_model.pkl:
  Pre-trained XGBoost regression model saved using pickle.

📌 Notes:
-----------------------
- HTML files are stored inside the `templates` folder as required by Flask.
- app.py and model.pkl must be in the same directory for model loading to work properly.
- The model expects exactly the same order and number of features as during training.

💻 To Run:
-----------------------
1. Open terminal or VS Code and navigate to this folder
2. Run: python app.py
3. Open browser: http://127.0.0.1:5000
