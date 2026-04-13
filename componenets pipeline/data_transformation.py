import pandas as pd

class DataTransformation:
    def initiate_data_transformation(self, train_path, test_path):
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        X_train = train_df.drop("target", axis=1)
        y_train = train_df["target"]

        X_test = test_df.drop("target", axis=1)
        y_test = test_df["target"]

        return X_train, X_test, y_train, y_test
    