import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)