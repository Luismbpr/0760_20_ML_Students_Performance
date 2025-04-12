import numpy as np
import pandas as pd

from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler

#from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.pipeline.predict_pipeline import CustomData
from src.pipeline.predict_pipeline import PredictPipeline

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
      In home.html will be the input fields for the model to do the prediction
    
    POST
      Returns 
    
    .
    """
    if request.method=='GET':
        return render_template('home.html')
    else:
        #pass
        ## from src.pipeline.predict_pipeline
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score')),
        )
        ## CustomData.get_data_as_data_frame
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(features=pred_df)
        print("After Prediction")
        return render_template('home.html', results=results[0])
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")