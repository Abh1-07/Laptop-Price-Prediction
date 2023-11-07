import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import evaluate_model
from src.utils import save_object
from dataclasses import dataclass
#models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score


@dataclass
class Model_trainer_config:
    model_trainer_obj_path = os.path.join('Artifacts','model.pkl')

    
class Model_trainer:
    
    def __init__(self):
        self.model_trainer_config = Model_trainer_config()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                'Linear Regression': LinearRegression(),
                'K-Neighbors Regressor': KNeighborsRegressor(),
                'Decision Tree': DecisionTreeRegressor(),
                'Random Forest Regressor': RandomForestRegressor(),
                'XGBRegressor': XGBRegressor(),
                "Cat Boosting": CatBoostRegressor(),
                'Ada Boosting': AdaBoostRegressor()
            }

            models_report: dict = evaluate_model(x_train, y_train, x_test, y_test, models)

            best_model_score = max(sorted(list(models_report.values())))
            best_model_name = list(models_report.keys())[list(models_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No Best Model Found!")
            save_object(
                file_path=self.model_trainer_config.model_trainer_obj_path,
                obj = best_model
            )
            predicted_best_model = best_model.predict(x_test)
            r2_square = r2_score(y_test, predicted_best_model)
            return r2_square
        except Exception as e:
            raise CustomException(e, sys)
        
