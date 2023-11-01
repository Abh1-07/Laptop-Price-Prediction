import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestConfig:
    train_data_path = os.path.join('Artifacts', 'train.csv')
    test_data_path = os.path.join('Artifacts', 'test.csv')
    raw_data_path = os.path.join('Artifacts', "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Enter the Data Ingestion Method/Component")
        try:
            data = pd.read_csv("notebooks\Processed data.csv")
            logging.info('Data Extracted and read as a DataFrame')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train Test Split on DataFrame Initiated')
            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data Ingestion Completed")

            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
                )

        except Exception as e:
            raise CustomException(e, sys)
if __name__ == '__main__':

    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
        
