
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

warnings.filterwarnings(action='ignore')

import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test')

mycursor=mydb.cursor()
mycursor.execute("select 1CApp_Name from newtable")
pt=[]
ptt=[]
for i in mycursor:
    if i not in pt:
        pt.append(i)

print(pt)
