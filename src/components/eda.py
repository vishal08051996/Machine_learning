import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion

EDA_DIR = "reports/eda"
os.makedirs(EDA_DIR, exist_ok=True)

class EDA:
    def __init__(self, df):
        self.df = df

    def check_missing_values(self):
        """Checks for missing values in the dataset."""
        try:
            missing_values = self.df.isnull().sum()
            missing_report = pd.DataFrame(missing_values, columns=['Missing Count'])
            missing_report["Missing Percentage"] = (missing_report["Missing Count"] / len(self.df)) * 100

            missing_report.to_csv(os.path.join(EDA_DIR, "missing_values.csv"), index=True)
            logging.info("Missing values analysis saved.")

            return missing_report

        except Exception as e:
            raise CustomException(f"Error in missing values check: {str(e)}")

    def basic_statistics(self):
        """Generates basic statistics of the dataset."""
        try:
            stats = self.df.describe()
            stats.to_csv(os.path.join(EDA_DIR, "basic_statistics.csv"), index=True)
            logging.info("Basic statistics saved.")
            return stats

        except Exception as e:
            raise CustomException(f"Error in basic statistics: {str(e)}")

    def plot_distributions(self):
        """Plots distribution of numerical features."""
        try:
            num_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
            plt.figure(figsize=(12, 6))
            
            for i, col in enumerate(num_cols[:5]):  # Plot first 5 features
                plt.subplot(2, 3, i + 1)
                sns.histplot(self.df[col], kde=True)
                plt.title(f"Distribution of {col}")
            
            plt.tight_layout()
            plt.savefig(os.path.join(EDA_DIR, "feature_distributions.png"))
            logging.info("Feature distributions saved.")

        except Exception as e:
            raise CustomException(f"Error in plotting distributions: {str(e)}")

    def correlation_matrix(self):
        """Generates correlation heatmap."""
        try:
            plt.figure(figsize=(10, 6))
            sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Matrix")
            plt.savefig(os.path.join(EDA_DIR, "correlation_matrix.png"))
            logging.info("Correlation matrix saved.")

        except Exception as e:
            raise CustomException(f"Error in correlation matrix: {str(e)}")

    def run(self):
        """Executes all EDA steps."""
        logging.info("EDA Started")
        print(self.check_missing_values())
        print(self.basic_statistics())
        self.plot_distributions()
        self.correlation_matrix()
        logging.info("EDA Completed")


if __name__ == "__main__":
    obj = DataIngestion()
    df = obj.run()  # Get data from ingestion
    eda_obj = EDA(df)
    eda_obj.run()
