import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pickle

from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


def save_object(file_path, obj):
    """
    Saves object. Saves pickle file object
    from src.utils import save_object
    save_object(file_path=, obj=)
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with os.open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluates models, performs Grid Search, Selects the best parameters
    Selects the best models trains the model and performs metric evaluation
    from src.utils import evaluate_models
    evaluate_models(X_train=, y_train=, X_test=, y_test=, models=, param=)
    """
    try:
        #pass
        report = {}

        for i in range(len(list(models))):
            #print(i)##for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(estimator=model, param_grid=para)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.git(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_true=y_train, 
            y_pred=y_train_pred)
            test_model_score = r2_score(y_true=y_test, y_pred=y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        
        return report
    
    except Exception as e:
        raise CustomException(e, sys)
