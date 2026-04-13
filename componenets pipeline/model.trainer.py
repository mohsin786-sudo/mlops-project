from sklearn.linear_model import LogisticRegression

class ModelTrainer:
    def initiate_model_trainer(self, X_train, y_train):
        model = LogisticRegression()
        model.fit(X_train, y_train)
        return model