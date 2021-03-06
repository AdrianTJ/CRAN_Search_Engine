
# Imports
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import dump

# Load the data, as packages
packages = pd.read_csv("../data/packages_11_may_2022.csv")

# Create the TF-IDF model, called vectors
vectorizer = TfidfVectorizer(lowercase=True, strip_accents='unicode', stop_words='english')
vectors = vectorizer.fit_transform(packages['Description'])

# Joblib dump model, saved as `tf-idf.joblib`
dump(vectors, 'tf-idf.joblib') 