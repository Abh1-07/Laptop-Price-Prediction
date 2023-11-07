import os 
import sys
import dill
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        # saving the pickle model to desired place
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
        logging.info('Pickle file made and dumped with data')
    except Exception as e:
        raise CustomException(e,sys)    

def evaluate_model(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(x_train,y_train)

            y_predict_train = model.predict(x_train)
            y_predict_test = model.predict(x_test)

            model_train_r2sq = r2_score(y_train, y_predict_train)
            model_test_r2sq = r2_score(y_test, y_predict_test)
            report[list(models.keys())[i]] = model_test_r2sq
        return report

    except Exception as e:
        raise CustomException(e, sys)
