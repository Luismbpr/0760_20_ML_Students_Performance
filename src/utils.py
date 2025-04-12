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

## For RandomizedSearchCV
#from sklearn.model_selection import RandomizedSearchCV
#from scipy.stats import uniform


def save_object(file_path, obj):
    """
    Saves object. Saves pickle file object
    from src.utils import save_object
    save_object(file_path=, obj=)

    Note: When using RandomizedSearchCV
    Example of using it
    from sklearn.model_selection import RandomizedSearchCV
    from scipy.stats import uniform
    param_dist = {
    'C': uniform(0.1, 10),  # Uniform distribution between 0.1 and 10
    'kernel': ['linear', 'rbf', 'poly'],
    'gamma': ['scale', 'auto'] + list(np.logspace(-3, 3, 50))
    }
    # Create the RandomizedSearchCV object
    randomized_search = RandomizedSearchCV(estimator=baseline_svm, param_distributions=param_dist, n_iter=20, cv=5)
    
    randomized_search.fit(X_train, y_train)
    
    # Get the best hyperparameters and model
    best_params_rand = randomized_search.best_params_
    best_model_rand = randomized_search.best_estimator_
    
    # Evaluate the best model
    y_pred_best_rand = best_model_rand.predict(X_test)
    accuracy_best_rand = accuracy_score(y_test, y_pred_best_rand)
    print(f"Best SVM Accuracy: {accuracy_best_rand:.2f}")
    print(f"Best Hyperparameters: {best_params_rand}")
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        ## Error. It is not with os.open()
        #with os.open(file_path, "wb") as file_obj:
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):
    """
    Loads object. Loads pickle file object
    Args
      file_path: str - Object file path to be loaded
    
    from src.utils import load_object
    load_object(file_path=)
    """
    try:
        #pass
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)



def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]
            
            ## If Using RandomizedSearchCV
            #rs = RandomizedSearchCV(model, param_distributions=para,cv=3)
            #rs.fit(X_train, y_train)
            #best_params_rand = model.set_params(**rs.best_params_)
            ##best_model_rand = rs.best_estimator_

            ## If using GridSearchCV
            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            ## Unpack the dictionary
            model.set_params(**gs.best_params_)
            #model = model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        
        return report

    except Exception as e:
        raise CustomException(e, sys)



# def evaluate_models(X_train, y_train, X_test, y_test, models, param):
#     """
#     Evaluates models, performs Grid Search, Selects the best parameters
#     Selects the best models trains the model and performs metric evaluation
#     from src.utils import evaluate_models
#     evaluate_models(X_train=, y_train=, X_test=, y_test=, models=, param=)

#     Args
#       X_train
#       y_train
#       X_test
#       y_test
#       models
#       param

#       Calculates R2_Score

#     Returns
#       Report: dict Report
    
#       from src.utils import evaluate_models
#       evaluate_models(X_train=, y_train=, X_test=, y_test=, models=, param=)
#     """
#     try:
#         #pass
#         report = {}

#         for i in range(len(list(models))):
#             model = list(models.values())[i]
#             para=param[list(models.keys())[i]]

#             gs = GridSearchCV(model, para, cv=3)
#             gs.fit(X_train, y_train)
#             #model.fit(X_train, y_train)
            
#             ## Getting best parameters and training the model with them
#             model.set_params(**gs.best_params_)
#             model.fit(X_train,y_train)

#             y_train_pred = model.predict(X_train)
#             y_test_pred = model.predict(X_test)

#             train_model_score = r2_score(y_train, 
#                                          y_train_pred)
            
#             test_model_score = r2_score(y_test,
#                                         y_test_pred)
            
#             report[list(models.keys())[i]] = test_model_score
#         logging.info(f"Returning Report from utils.evaluate_models function")
#         return report
    
#     except Exception as e:
#         raise CustomException(e, sys)
