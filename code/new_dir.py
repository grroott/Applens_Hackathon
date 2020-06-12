import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
dataset = [["I liked      the movie", "positive","d"],
           ["It’s a good movie. Nice story", "positive","d"],
           ["Hero’s acting is bad but heroine looks good. Overall nice movie", "positive","d"],
           ["Nice songs. But sadly boring ending.", "negative","d"]]
dataset = pd.DataFrame(dataset)
dataset.columns = ["Text", "Reviews","Extr"]
# nltk.download('stopwords')
corpus = []
for i in range(0, 4):
    text = re.sub('[^a-zA-Z]', '', dataset['Text'],dataset["Extr"][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = ''.join(text)
    corpus.append(text)
print(corpus)
# creating bag of words model
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
print("c")
y = dataset.iloc[:, 1].values
print(y)
# splitting the data set into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25)
# fitting naive bayes to the training set
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
classifier = GaussianNB();
classifier.fit(X_train, y_train)
# predicting test set results
y_pred = classifier.predict(X_test)
yy_pred = classifier.predict(X_train)
print("########")
print(y_pred)
print(y_test)
f = open('my_classifier.pickle', 'wb')
pickle.dump(classifier, f)
f.close()
# making the confusion matrix
cm = confusion_matrix(y_test, y_pred)

