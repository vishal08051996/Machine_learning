import os
import pandas as pd
import numpy as np
from src.components.data_ingestion import DataIngestion
from src.components.data_preprocessing import DataPreprocessing
from src.components.model import StrengthPredictionModel
from src.logger import logging
from src.exception import CustomException

class TrainPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_preprocessing = DataPreprocessing()
        self.model = StrengthPredictionModel()

    def run_pipeline(self):
        try:
            logging.info("Starting Training Pipeline...")

            # Step 1: Data Ingestion
            raw_data_path = self.data_ingestion.ingest_data()
            
            # Step 2: Data Preprocessing
            processed_data_path = self.data_preprocessing.preprocess_data(raw_data_path)
            df = pd.read_csv(processed_data_path)
            X = df.drop(columns=['strength'])
            y = df['strength']

            # Step 3: Train Model
            self.model.train(X, y)

            logging.info("Training Pipeline Completed Successfully!")

        except Exception as e:
            raise CustomException(f"Error in Training Pipeline: {str(e)}")

if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
