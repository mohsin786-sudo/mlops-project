from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return "MLOps Project Running 🚀"

@app.route('/predict')
def predict():
    return "Prediction: [0]"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
