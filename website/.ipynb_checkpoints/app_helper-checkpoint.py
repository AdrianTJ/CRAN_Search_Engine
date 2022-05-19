import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from joblib import load

packages = pd.read_csv("../data/packages_11_may_2022.csv")
vectors = load('../tf-idf.joblib')

def get_closest(query, w = 0.5, sort_by = "PageRank"):
    vectorizer = TfidfVectorizer(lowercase=True, strip_accents='unicode', stop_words='english')
    result = vectorizer.fit(packages['Description']).transform([query]) 
    pairwise_similarity = result * vectors.T

    indexes = (-pairwise_similarity.toarray()[0]).argsort()[:20]
    
    df = [packages["Package"], 
      packages["Version"], 
      packages["Title"], 
      packages["Description"], 
      packages["page.rank"],
      pd.Series(pairwise_similarity.toarray()[0])]

    headers = ["Package_name", "Version", "Title", "Description", "PageRank", "PW_Similarity"]

    df = pd.concat(df, axis=1, keys=headers)
    df["Mix"] = df["PageRank"]*df["PW_Similarity"]
    #df["Mix"] = w*df["PageRank"] + (1-w)*df["PW_Similarity"]
    df = df.iloc[indexes].sort_values(by = [sort_by], ascending=False).reset_index()
    return df