import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pickle

from src.exception import CustomException
from src.logger import logging


def save_object(file_path, obj):
    """
    Saves object. Saves pickle file object
    from src.utils import save_object
    save_object(file_path=, obj=)
    """
    try:
        with os.open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e,sys)