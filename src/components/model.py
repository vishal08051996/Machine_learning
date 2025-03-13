from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

class StrengthPredictionModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        """Build ANN model"""
        try:
            model = Sequential([
                Dense(64, activation='relu', input_shape=(5,)),  # Assuming 5 input features
                Dense(32, activation='relu'),
                Dense(16, activation='relu'),
                Dense(1)  # Output layer
            ])
            model.compile(optimizer=Adam(), loss='mse', metrics=['mae'])
            logging.info("ANN Model built successfully.")
            return model
        except Exception as e:
            raise CustomException(f"Error in building model: {str(e)}")

    def train(self, X, y):
        """Train the ANN Model"""
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)
            self.model.save(os.path.join(MODEL_DIR, "ann_model.h5"))
            logging.info("Model trained and saved successfully.")
        except Exception as e:
            raise CustomException(f"Error in training model: {str(e)}")
