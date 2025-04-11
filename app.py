import numpy as np
import pandas as pd

from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler

#from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application

## Route for home page
@app.route("/")
def index():
    return render_template("index.html")

## Route for prediction page
@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    """
    GET
      Returns the default home page
      input fields for the model to do the prediction
    
    POST
      Returns 
    """
    if request.method=='GET':
        return render_template('home.html')
    else:
        pass

