import os
import shutil
import pandas as pd
from src.logger import logging
from src.exception import CustomException

RAW_DATA_DIR = "data/raw"

class DataIngestion:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def move_file(self):
        """
        Moves the dataset from user-provided location to `data/raw/`
        """
        try:
            if not self.file_path:
                self.file_path = input("Enter the dataset file path: ").strip()

            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"File not found: {self.file_path}")

            os.makedirs(RAW_DATA_DIR, exist_ok=True)
            dest_path = os.path.join(RAW_DATA_DIR, os.path.basename(self.file_path))
            shutil.copy(self.file_path, dest_path)

            logging.info(f"File successfully moved to {dest_path}")
            return dest_path

        except Exception as e:
            raise CustomException(f"Error in moving file: {str(e)}")

    def read_data(self, file_path):
        """
        Reads the dataset and returns a Pandas DataFrame.
        """
        try:
            ext = os.path.splitext(file_path)[-1].lower()
            if ext == ".csv":
                df = pd.read_csv(file_path)
            elif ext in [".xls", ".xlsx"]:
                df = pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file format! Use CSV or Excel.")
            
            logging.info(f"Data successfully loaded with shape: {df.shape}")
            return df

        except Exception as e:
            raise CustomException(f"Error in reading data: {str(e)}")

    def run(self):
        """
        Executes the data ingestion process.
        """
        try:
            file_path = self.move_file()
            df = self.read_data(file_path)
            logging.info(f"Data Ingestion Completed. Data Shape: {df.shape}")
            return df  # Returning DataFrame for next step (EDA)

        except Exception as e:
            raise CustomException(f"Data Ingestion Failed: {str(e)}")

if __name__ == "__main__":
    obj = DataIngestion()
    df = obj.run()  # Now pass `df` to EDA
