
# Imports
import pandas as pd
import numpy as np
from joblib import load

def get_closest(query):
  vectors = load('tf-idf.joblib') 
  result = vectorizer.fit(packages['Description']).transform([query])
  pairwise_similarity = result * vectors.T

  indexes = (-pairwise_similarity.toarray()[0]).argsort()[:20]

  return packages.iloc[indexes].sort_values(by = ['page.rank'], ascending=False)