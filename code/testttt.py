import pickle
import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
dataset = ["Reports issue in AVM PMOAVM PMO - Reports issue in AVM PMONone597603 1/14/2019 4:10:14 PM\xa0\xa0WIP\xa0\xa0SRI RAM\xa0\xa0\xa0\xa0625820 1/14/2019 4:05:59 PM\xa0\xa0Hi\xa0\xa0Team,\xa0\xa0Please change the status of the SO 30989171\xa0\xa0to '1.2 Pending Demand Validation'\xa0\xa0Regards AVMTechdesk\xa0\xa0Keerthana G S\xa0\xa0\xa0Please change the status of the SO 30989171\xa0\xa0to '1.2 Pending Demand Validation'597603 1/14/2019 4:11:21 PM\xa0\xa0\xa0status of the SO 30989171 updated to '1.2 Pending Demand Validation'\xa0\xa0SRI RAM\xa0\xa0\xa0 AVMPMO_L2 AVM PMO", 'AVMPMO']
dataset = pd.DataFrame(dataset)
dataset.columns = ["Text"]
nltk.download('stopwords')
corpus = []
for i in range(0, 1):
    text = re.sub('[^a-zA-Z]', '', dataset['Text'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = ''.join(text)
    corpus.append(text)
# creating bag of words model
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
# fitting naive bayes to the training set
f = open('my_classifier.pickle', 'rb')
classifier = pickle.load(f)
print(classifier.predict(X))
f.close()