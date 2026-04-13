import pickle
import pandas as pd

class PredictPipeline:
    def predict(self, features):
        with open("artifacts/model.pkl", "rb") as f:
            model = pickle.load(f)

        data = pd.DataFrame(features)
        prediction = model.predict(data)

        return prediction