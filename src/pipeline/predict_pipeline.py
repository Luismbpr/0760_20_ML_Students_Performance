import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        """
        from src.pipeline.predict_pipeline import predict
        predict(features=)
        """
        try:
            #pass
            model_path=os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")
            print("Before Loading Model and preprocessor")
            logging.info("predict_pipeline - Before Loading #model and preprocessor")
            model = load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading model and preprocessor")
            #logging.info("predict_pipeline - After Loading model and preprocessor")
            #logging.info("predict_pipeline - Scaling Data")
            print("Before Scaling Data")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            print("After Scaling Data")
            #logging.info("predict_pipeline - Scaling Data")
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)

#"lunch": ["standard", "free/reduced"]
#"test_preparation_course": ["none", "completed"]}
#"writing_score"
#"reading_score"
#"parental_level_of_education":[ "some college", "associate's degree", "high school", "some high school", "bachelor's degree", "master's degree"]
#"race_ethnicity": ["group C", "group D", "group B", "group E", "group A"]
#{"gender":["female", "male"]


class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education:str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int,
                 ):
         """
         from src.pipeline.predict_pipeline import CustomData
         CustomData.get_data_as_data_frame(gender=,race_ethnicity=,
         parental_level_of_education=, lunch=, test_preparation_course=, reading_score=, writing_score=)
         """
         self.gender = gender
         self.race_ethnicity = race_ethnicity
         self.parental_level_of_education = parental_level_of_education
         self.lunch = lunch
         self.test_preparation_course = test_preparation_course
         self.reading_score = reading_score
         self.writing_score = writing_score
    
    def get_data_as_data_frame(self):
        try:
            #pass
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)