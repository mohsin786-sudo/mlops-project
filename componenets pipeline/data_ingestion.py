import pandas as pd
import os

class DataIngestion:
    def__init__(self):
    self.train_path = "artifacts/train.csv"
    self.test_path = "artifacts/test.csv"

    def initiate_data_ingestion(self):
        os.makedirs("artifacts", exist_ok=True)

        # dummy dataset
        data = {
            "feature1":[1, 2, 3, 4 ],
            "feature2":[5, 6, 7, 8 ],
             "target":[0, 1, 0, 1]
        }