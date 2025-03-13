import os
import pandas as pd
import numpy as np
import tensorflow as tf
from src.logger import logging
from src.exception import CustomException

MODEL_PATH = "models/ann_model.h5"

class PredictPipeline:
    def __init__(self, input_data):
        self.input_data = input_data

    def load_model(self):
        """Load trained ANN model"""
        try:
            model = tf.keras.models.load_model(MODEL_PATH)
            logging.info("Model Loaded Successfully!")
            return model
        except Exception as e:
            raise CustomException(f"Error in loading model: {str(e)}")

    def make_prediction(self):
        """Make predictions using the trained model"""
        try:
            model = self.load_model()
            prediction = model.predict(np.array([self.input_data]))
            logging.info(f"Prediction: {prediction}")
            return prediction
        except Exception as e:
            raise CustomException(f"Error in making prediction: {str(e)}")

if __name__ == "__main__":
    sample_input = [200, 50, 30, 400, 20]  # Example Input
    predictor = PredictPipeline(sample_input)
    result = predictor.make_prediction()
    print(f"Predicted Strength: {result}")
