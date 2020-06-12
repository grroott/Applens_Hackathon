import openpyxl
import pandas as pd

import numpy as np
import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

path="E:\\1500to1600.xlsx"
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active


for i in range(2,9):
    x = ""
    final_lstt = []
    for j in range(1,3):
        cell_obj = sheet_obj.cell(row = i, column = j)
        x=x+" "+str(cell_obj.value)
    final_lstt.append(x)
    print(final_lstt)
    final_lstt = pd.DataFrame(final_lstt)
    final_lstt.columns = ["Details"]
    # nltk.download('stopwords')
    corpus = []
    for i in range(0, len(final_lstt)):
        text = re.sub('[^a-zA-Z]', '', final_lstt['Details'][i])
        text = text.lower()
        text = text.split()
        ps = PorterStemmer()
        text = ''.join(text)
        corpus.append(text)
    # creating bag of words model
    print(corpus)
    cv = CountVectorizer(max_features=1500)
    X = cv.fit_transform(corpus).toarray()
    print(X)
    # fitting naive bayes to the training set
    f = open('my_classifier1.pickle', 'rb')
    classifier = pickle.load(f)
    print(classifier.predict(X))



f.close()

