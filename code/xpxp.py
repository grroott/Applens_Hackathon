import mysql.connector
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re

warnings.filterwarnings(action='ignore')
final_lst = []
mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test')


final_lst=[]

for iii in range(1,1000):
    mycursor = mydb.cursor()
    sql="select * from newtablee where row_count=(%s)"
    form=(iii,)
    mycursor.execute(sql,form)
    pt = []
    for i in mycursor:
        for j in i:
            try:
                j = j.replace(u'\xa0', u'')
            except:
                pass
            pt.append(j)

    vip=[]
    non_vip=[]
    for b in pt:
        if b == pt[0] or b == pt[1] or b == pt[8]:
            vip.append(b)
        else:
            non_vip.append(b)
    ptt = []
    for i in non_vip:
        x = i.split(" ")
        ptt.append(x)

    pttt = []
    for i in ptt:
        for j in i:
            pttt.append(j)

    lst = []
    lstt = []

    def Punctuation(string):
        punctuations = '''!()-[]{};:'"\,<>'"./?@#$%^&*_~'''
        for i in punctuations:
            lst.append(i)
        for i in pttt:
            if i not in lst:
                lstt.append(i)

    string = pttt
    Punctuation(string)

    for i in lstt:
        if i == '':
            lstt.remove(i)

    strr = ''
    for b in lstt:
        strr = strr + " " + b

    s = " ".join(strr.split())
    example_sent = s
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(example_sent)
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    ls = []
    lss = []
    punctuations = '''!()-[]{};:'"\,<>'"./?@#$%^&*_~'''
    for i in punctuations:
        ls.append(i)
    for i in filtered_sentence:
        if i not in lst:
            lss.append(i)
    ps = PorterStemmer()

    words = lss
    words_aft_root = []
    for w in words:
        words_aft_root.append(ps.stem(w))

    lemmatizer = WordNetLemmatizer()
    words_aft_lem = []
    for i in words_aft_root:
        words_aft_lem.append(lemmatizer.lemmatize(i))
    lower_case = []
    for i in words_aft_lem:
        lower_case.append(i.lower())
    lower_case.pop()
    lower_cas = []
    for i in lower_case:
        pattern = re.compile(r'\d[:/]\d\d[:/]\d\d')
        patternn=re.compile(r'\d\d\d\d\d\d')
        matches = pattern.finditer(i)
        matchess = patternn.finditer(i)
        count = 0
        for match in matches:
            count += 1
        for match in matchess:
            count += 1
        if i not in lower_cas:
            if count == 0:
                lower_cas.append(i)
    for i in vip:
        lower_cas.append(i)

    lower_ca=[]

    for i in lower_cas:

        pattern = re.compile(r'\d[:/]\d[:/]\d\d\d\d')
        matches = pattern.finditer(i)
        count = 0
        for match in matches:
            count += 1
        if count == 0:
            lower_ca.append(i)

    final_lst.append(lower_ca)

print("traning inp")

model1 = gensim.models.Word2Vec(final_lst, min_count=1,size=100, window=5)

model1.save('thousand_sample_cbow_v2')

model2 = gensim.models.Word2Vec(final_lst, min_count = 1, size = 100, window = 5, sg = 1)

model2.save('thousand_sample_skipgram_v2')