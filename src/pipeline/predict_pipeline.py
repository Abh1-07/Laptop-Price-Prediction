import pandas as pd
import numpy as np
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictionPipeline:

    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path = "Artifacts\model.pkl"
            preprocessor_path = "Artifacts\preprocessor.pkl"
            loaded_model = load_object(filepath=model_path)
            loaded_preprocessor = load_object(filepath=preprocessor_path)
            scaled_data = loaded_preprocessor.transform(features)
            prediction = loaded_model.predict(scaled_data)
            return np.exp(prediction)
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,Company, TypeName,Ram,Gpu,Weight,Touchscreen,Ips,x_res,y_res,inches, CpuName, HDD, SSD, OS):
        self.Company = Company
        self.TypeName = TypeName
        self.Ram = Ram
        self.Gpu = Gpu
        self.Weight = Weight
        self.Touchscreen = Touchscreen
        self.Ips = Ips
        self.x_res = x_res
        self.y_res = y_res
        self.inches = inches
        self.CpuName = CpuName
        self.HDD = HDD
        self.SSD = SSD
        self.OS = OS

    def get_data_as_dataframe(self):
        try:
            custom_df =  {
                'Company' : [self.Company],
                'TypeName' : [self.TypeName],
                'Ram' : [int(self.Ram)],
                'Gpu': [self.Gpu],
                'Weight' : [float(self.Weight)],
                'Touchscreen' : [int(self.Touchscreen)],
                'Ips' : [int(self.Ips)],
                'Ppi' : [(int(self.x_res) * int(self.y_res)) / float(self.inches)],
                'Cpu Name' : [self.CpuName],
                'HDD' : [int(self.HDD)],
                'SSD' : [int(self.SSD)],
                'OS' : [self.OS]
            }
            print(custom_df)
            return pd.DataFrame(custom_df)
        except Exception as e:
            raise CustomException(e, sys)