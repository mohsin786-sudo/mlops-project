import pandas as pd
import os

class DataIngestion:
    def __init__(self):
        self.train_path = "artifacts/train.csv"
        self.test_path = "artifacts/test.csv"

    def initiate_data_ingestion(self):
        os.makedirs("artifacts", exist_ok=True)

        data = {
            "feature1": [1, 2, 3, 4],
            "feature2": [5, 6, 7, 8],
            "target": [0, 1, 0, 1]
        }

        df = pd.DataFrame(data)

        df.to_csv(self.train_path, index=False)
        df.to_csv(self.test_path, index=False)

        return self.train_path, self.test_path