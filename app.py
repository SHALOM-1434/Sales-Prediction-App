# app.py

# ▶️ Import Libraries
import pickle  # For loading the saved model
import numpy as np
from flask import Flask, request, render_template

# ▶️ Initialize Flask App
app = Flask(__name__)

# ▶️ Load the Trained Model (.pkl file must match this folder path)
with open('xgb_sales_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ▶️ Home Route: Loads the form
@app.route('/')
def home():
    return render_template('index.html')

# ▶️ Predict Route: Receives input from HTML form and returns prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetch inputs from form and convert to float
        features = [
            float(request.form['Store']),
            float(request.form['DayOfWeek']),
            float(request.form['Open']),
            float(request.form['Promo']),
            float(request.form['SchoolHoliday']),
            float(request.form['CompetitionDistance']),
            float(request.form['CompetitionOpenSinceMonth']),
            float(request.form['CompetitionOpenSinceYear']),
            float(request.form['Promo2']),
            float(request.form['Promo2SinceWeek']),
            float(request.form['Promo2SinceYear']),
            float(request.form['Year']),
            float(request.form['Month']),
            float(request.form['Day']),
            float(request.form['WeekofYear']),
            float(request.form['IsWeekend']),
            float(request.form['IsPromoMonth']),
            float(request.form['CompetitionOpenTimeMonths']),
            float(request.form['StoreType_b']),
            float(request.form['StoreType_c']),
            float(request.form['StoreType_d']),
        ]

        # Reshape input to match model expectations
        input_array = np.array(features).reshape(1, -1)

        # Make Prediction
        prediction = model.predict(input_array)[0]

        # Render result
        return render_template('result.html', prediction_text=f"Predicted Sales: ₦{prediction:,.2f}")

    except Exception as e:
        return render_template('result.html', prediction_text=f"An error occurred: {str(e)}")

# ▶️ Run the Flask App Locally
if __name__ == '__main__':
    app.run(debug=True)
