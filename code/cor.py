import pandas as pd
import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import mysql.connector
import warnings
warnings.filterwarnings(action='ignore')
mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='test')
final_lst = []
for iii in range(1, 20):
    mycursor = mydb.cursor()
    # sql = "select Item,Summary from newtablee where row_count=(%s)"
    # form = (iii,)
    # mycursor.execute(sql, form)
    strr = ''
    lst = []
    # for i in mycursor:
    #     for j in i:
    #         strr = strr+" " + j
    sql = "select Assigned_to_Group,Category from newtablee where row_count=(%s)"
    form = (iii,)
    mycursor.execute(sql, form)
    for i in mycursor:
        for j in i:
            strr = strr + " " + j
    lst.append(strr)
    sql = "select 1CApp_Name from newtablee where row_count=(%s)"
    form = (iii,)
    mycursor.execute(sql, form)
    for i in mycursor:
        for j in i:
            lst.append(j)
    final_lst.append(lst)

    print(lst)
final_lst = pd.DataFrame(final_lst)
final_lst.columns = ["Details", "Appname"]
# nltk.download('stopwords')
corpus = []
for i in range(0, 19):
    text = re.sub('[^a-zA-Z]', '', final_lst['Details'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = ''.join(text)
    print(text)
    corpus.append(text)
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
y = final_lst.iloc[:, 1].values
# splitting the data set into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33)
# fitting naive bayes to the training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB();
classifier.fit(X_train, y_train)
f = open('my_classifier1.pickle', 'wb')
pickle.dump(classifier, f)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,classifier.predict(X_test)))
print(classifier.predict(X_test))

print(y_test)

f.close()