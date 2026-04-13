from src.pipeline.predict_pipeline import PredictPipeline

if __name__ == "__main__":
    data = [[2, 6]]

    pipeline = PredictPipeline()
    result = pipeline.predict(data)

    print("Prediction:", result)
