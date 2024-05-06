import os
import sys
import pandas as pd

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomExecptionHandler
from src.logger import logging

@dataclass
class DataIngestionConfig :
    train_data_path : str = os.path.join("artifacts", "train.csv")
    test_data_path : str = os.path.join("artifacts", "test.csv")
    raw_data_path : str = os.path.join("artifacts", "raw.csv")

class DataIngestion : 
    def __init__(self) : 
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) :
        logging.info("Enter the data ingestion method or component")
        try : 
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Reading dataset as data frame')

            folder_path = os.path.dirname(self.ingestion_config.train_data_path)
            os.makedirs(folder_path, exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e: 
            raise CustomExecptionHandler(e, sys)
        
if __name__ == "__main__" :
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()