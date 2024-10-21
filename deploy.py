import pickle
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Load the saved model
model_path = "model.pkl"  # Update this to your actual model path
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Assuming data comes in the correct format
    prediction = model.predict([data['input_features']])  # Adjust based on your model's input
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    # Bind to host and port. Adjust as needed.
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
