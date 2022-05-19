from flask import Flask,request, url_for, redirect, render_template
#import pickle
#import numpy as np

import pandas as pd
import numpy as np
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer
import app_helper

app = Flask(__name__, template_folder='templates')

@app.route('/') 
def hello_world():
    return render_template("search_engine.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    features=[x for x in request.form.values()]
    if features[1] == "": 
        df = app_helper.get_closest(features[0], sort_by = "PageRank") # default if not provided
    else: 
        df = app_helper.get_closest(features[0], sort_by = features[1])
    return render_template('search_engine.html',  tables=[df.to_html(classes='data', header="true")]) 

if __name__ == '__main__':
    app.run(debug=True)
