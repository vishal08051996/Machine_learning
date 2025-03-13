import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

class DataPreprocessing:
    def __init__(self, df):
        self.df = df

    def handle_missing_values(self):
        """Handles missing values by filling with mean for numerical and mode for categorical."""
        try:
            for col in self.df.columns:
                if self.df[col].dtype == 'object':  # Categorical
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
                else:  # Numerical
                    self.df[col].fillna(self.df[col].mean(), inplace=True)

            logging.info("Handled missing values successfully.")
        except Exception as e:
            raise CustomException(f"Error in handling missing values: {str(e)}")

    def scale_numerical_features(self):
        """Standardizes numerical features."""
        try:
            num_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
            scaler = StandardScaler()
            self.df[num_cols] = scaler.fit_transform(self.df[num_cols])

            logging.info("Numerical features scaled successfully.")
        except Exception as e:
            raise CustomException(f"Error in scaling numerical features: {str(e)}")

    def encode_categorical_features(self):
        """Encodes categorical features using Label Encoding."""
        try:
            cat_cols = self.df.select_dtypes(include=['object']).columns
            encoder = LabelEncoder()
            for col in cat_cols:
                self.df[col] = encoder.fit_transform(self.df[col])

            logging.info("Categorical features encoded successfully.")
        except Exception as e:
            raise CustomException(f"Error in encoding categorical features: {str(e)}")

    def save_processed_data(self):
        """Saves the cleaned and processed dataset."""
        try:
            self.df.to_csv(os.path.join(PROCESSED_DIR, "processed_data.csv"), index=False)
            logging.info("Processed data saved successfully.")

        except Exception as e:
            raise CustomException(f"Error in saving processed data: {str(e)}")

    def run(self):
        """Executes the full preprocessing pipeline."""
        logging.info("Data Preprocessing Started")
        self.handle_missing_values()
        self.scale_numerical_features()
        self.encode_categorical_features()
        self.save_processed_data()
        logging.info("Data Preprocessing Completed")
        return self.df


if __name__ == "__main__":
    obj = DataIngestion()
    df = obj.run()  # Fetch raw data from ingestion
    preprocessing_obj = DataPreprocessing(df)
    processed_df = preprocessing_obj.run()
    print("Processed Data Sample:\n", processed_df.head())
