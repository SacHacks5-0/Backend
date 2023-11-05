import os
from flask import Flask, request, jsonify
from model import train_model
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for local development
CORS(app)

trained_model = train_model()

@app.route('/predict', methods=['POST'])
def predict_loan_eligibility():
    try:
        data = request.get_json()

        age = float(data['age'])
        marital_status = int(data['marital_status'])
        income = float(data['income'])
        education_level = int(data['education_level'])
        loan_term = float(data['loan_term'])

        input_data = [[age, marital_status, income, education_level, loan_term]]

        prediction = predict(trained_model, input_data)

        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Run the Flask app locally
    app.run(host='localhost', port=5000, debug=True)
