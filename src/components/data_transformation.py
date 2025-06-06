import sys
import os
from dataclasses import dataclass
import pandas as pd
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformer_object(self):
        """
        This function Created the data transformation pipeline for all the columns.

        Numerical Pipeline
        Selects and transforms the Numerical columns
            SimpleImputer - Handles the missing values
            Performs Standard Scaling

        Categorical Pipeline
        Selects and transforms the Categorical columns
            SimpleImputer - Handles the missing values
            Performs OneHotEncoding
            Performs Standard Scaling

        Args
          .
          
        Returns
          preprocessor
        """
        try:
            #pass
            numerical_columns= [
                "reading_score",
                "writing_score"
            ]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            ## Pipelines
            ## SimpleImputer - Handles the missing values
            ## Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            ## Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")
            
            ## Merging both pipelines
            preprocessor = ColumnTransformer(
                [
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
    

    def initiate_data_transformation(self, train_path, test_path):
        """
        This function performs data transformation
        Args
          train_path
          test_path
        
        Returns
          train_arr
          test_arr
          self.data_transformation_config.preprocessor_obj_file_path
        
        from src.components.data_transformation import initiate_data_transformation

        initiate_data_transformation(train_path=, test_path=)
        """
        try:
            #pass
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Completed Reading Train and Test Data")
            logging.info("Obtaining Preprocessing Object")
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "math_score"
            numerical_columns= ["reading_score","writing_score"]
            #categorical_columns=["gender",
                                 #"race_ethnicity",
                                 #"parental_level_of_education",
                                 #"lunch",
                                 #"test_preparation_course"
                                 #]
            
            ## Selecting X and y
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"Applying preprocessing object on the training and testing dataframes.")

            ## Fit Transform Train - Transform Test
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            ## Concat Transformed data with target feature
            train_arr = np.c_[
                input_feature_train_arr,
                np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr,
                             np.array(target_feature_test_df)
            ]
            
            logging.info(f"Train and Test Array Created")
            ## Create/get function in utils/save_object()
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("Preprocessing Object Saved")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)