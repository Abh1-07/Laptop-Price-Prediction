import os
import sys
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import  SimpleImputer # TO handle missing values
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from dataclasses import dataclass
from src.utils import save_object

@dataclass
class Data_transform_config:
    preprocessor_obj_path = os.path.join('Artifacts','preprocessor.pkl')

class Data_transformation:
    def __init__(self):
        self.data_trans_config = Data_transform_config()
    
    def get_data_transformation_obj(self):
        try:
            cat_features = ['Company', 'TypeName', 'Gpu', 'Cpu Name', 'OS']
            num_features = ['Ram', 'Weight', 'Touchscreen', 'Ips', 'Ppi', 'HDD', 'SSD']
            num_pipe = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='median')),
                    ('Scaler',StandardScaler())
                         ]
            )
            logging.info(f'Numerical Features: {num_features}')
            cat_pipe = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ohe',OneHotEncoder(sparse=False,drop='first'))
                ]
            )
            logging.info(f"Categorial Features: {cat_features}")
            # combining both pipelines together
            preprocessor = ColumnTransformer(
                [
                    ('Num Pipeline', num_pipe, num_features),
                    ('Cat Pipeline', cat_pipe, cat_features)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Reading Train and Test data Completed')
            logging.info('Obtaining Preprocessing Object')

            preprocessing_obj = self.get_data_transformation_obj()
            output_column = 'Price'
            cat_features = ['Company', 'TypeName', 'Gpu', 'Cpu Name', 'OS']
            num_features = ['Ram', 'Weight', 'Touchscreen', 'Ips', 'Ppi', 'HDD', 'SSD']
            #making df for as x_train, x_test, y_train, y_test
            input_feature_train_df = train_df.drop(columns = [output_column])
            output_feature_train_df = np.log(train_df[output_column])
            input_feature_test_df = test_df.drop(columns=[output_column])
            output_feature_test_df = np.log(test_df[output_column])

            logging.info('Applying preprocessing object to training and testing DataFrame')
                # calling the saved pickle file as preprocessing_obj and doing fit_tranform on training dataset.
                # and transform on test dataset
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
                # combining the dataset and the transformed data of training and test set as array
            train_arr = np.c_[input_feature_train_arr, np.array(output_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(output_feature_test_df)]

            logging.info('Saving the preprocessor Model ')
            save_object(file_path =  self.data_trans_config.preprocessor_obj_path,obj = preprocessing_obj)
            return (
                train_arr,
                test_arr,
                self.data_trans_config.preprocessor_obj_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        