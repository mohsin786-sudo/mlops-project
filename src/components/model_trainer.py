from sklearn.linear_model import LogisticRegression
import pickle
import os

class ModelTrainer:
    def initiate_model_trainer(self, X_train, y_train):
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # save model
        os.makedirs("artifacts", exist_ok=True)
        with open("artifacts/model.pkl", "wb") as f:
            pickle.dump(model, f)

        return model