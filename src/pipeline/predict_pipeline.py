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
            model_path = "Artifacts/model.pkl"
            preprocessor_path = "Artifacts/preprocessor.pkl"
            loaded_model = load_object(filepath=model_path)
            loaded_preprocessor = load_object(filepath=preprocessor_path)
            scaled_data = loaded_preprocessor.transform(features)
            prediction = loaded_model.predict(scaled_data)
            return np.exp(prediction)
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,Company, TypeName,Ram,Gpu,Weight,Price,Touchscreen,Ips,x_resolution,y_resolution,inches, CpuName, HDD, SSD, OS):
        self.Company = Company
        self.TypeName = TypeName
        self.Ram = Ram
        self.Gpu = Gpu
        self.Weight = Weight
        self.Price = Price
        self.Touchscreen = Touchscreen
        self.Ips = Ips
        self.x_res = x_resolution
        self.y_res = y_resolution
        self.inches = inches
        self.CpuName = CpuName
        self.HDD = HDD
        self.SSD = SSD
        self.OS = OS

    def get_data_as_dataframe(self):
        try:
            custom_df =  {
                'Company' : self.Company,
                'TypeName' : self.TypeName,
                'Ram' : self.Ram,
                'Gpu': self.Gpu,
                'Weight' : self.Weight,
                'Touchscreen' : self.Touchscreen,
                'Ips' : self.Ips,
                'Ppi' : (self.x_res * self.y_res) / (self.inches),
                'Cpu Name' : self.CpuName,
                'HDD' : self.HDD,
                'SSD' : self.SSD,
                'OS' : self.OS
            }
            return pd.DataFrame(custom_df)
        except Exception as e:
            raise CustomException(e, sys)