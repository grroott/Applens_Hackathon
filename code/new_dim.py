# cleaning texts
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test')

# df=pd.read_sql("select * from zxc",con=mydb)


ptt=[]
mycursor = mydb.cursor()
for iii in range(1,10):
    sql="select * from zxc where row_count=(%s)"
    form=(iii,)
    mycursor.execute(sql,form)
    pt = []
    for i in mycursor:
        for j in i:
            pt.append(j)
    ptt.append(pt)

dataset = pd.DataFrame(ptt)
dataset.columns = [['Assigned_to_Group','Category','Item','Summary','Resolution','Support_Diary','Notes','Work_Log','1CApp_Name','row_count']]

nltk.download('stopwords')

corpus = []

for i in range(0, 5):
    text = re.sub('[^a-zA-Z]', '', dataset['Assigned_to_Group'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = ''.join(text)
    corpus.append(text)

# creating bag of words model
cv = CountVectorizer(max_features=1500)

X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 8].values
# X=df[['Assigned_to_Group','Category','Item','Summary','Resolution','Support_Diary','Notes','Work_Log']]
#
# Y=df[['1CApp_Name']]


# splitting the data set into training set and test set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)

# fitting naive bayes to the training set
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

classifier = GaussianNB();
classifier.fit(X_train, y_train)

# predicting test set results
y_pred = classifier.predict(X_test)

# making the confusion matrix
cm = confusion_matrix(y_test, y_pred)







# x=np.loadtxt(df)
# print(df.shape)
# print(X)
# print(Y)
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test= train_test_split(X,Y,test_size=0.2,random_state=10)
#
#
# print("d")
# from sklearn.linear_model import LinearRegression
# clf=LinearRegression()
#
# clf.fit(x_train,y_train)
#
# print(clf.predict(x_test))
# print('@@@@@@@')
# print(y_test)