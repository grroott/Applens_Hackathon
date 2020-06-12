# import openpyxl
# obb=openpyxl.load_workbook("E://testt_updated_v1.xlsx")
# o=obb.active
# col_name=[]
# tp=o.max_row
# o.cell(row=1,column=10).value='row_count'
# j=1
# for i in range(2,tp+1):
#     o.cell(row=i,column=10).value=j
#     j+=1
# obb.save("E://testt_updated_v1.xlsx")
# for i in range(1,11):
#     col_name.append(o.cell(row=1,column=i).value)
#
# joi=" varchar(100), ".join(col_name)+" varchar(100)"
#
# val_name=[]
# val_names=[]
# for j in range(2,1001):
#     val_name=[]
#     for i in range(1,11):
#         cx=str(o.cell(row=j, column=i).value)
#         val_name.append(cx)
#     val_name=tuple(val_name)
#     val_names.append(val_name)
#
# vari=(', '.join(['%s']*10))
#
# import mysql.connector
#
# mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test')
#
# mycursor=mydb.cursor()
# xx="create table if not exists newtablee ({temp})"
# mycursor.execute(xx.format(temp=joi))
# mycursor.execute("ALTER TABLE newtablee modify Work_Log varchar(6000)")
# mycursor.execute("ALTER TABLE newtablee modify Notes varchar(2000)")
# mycursor.execute("ALTER TABLE newtablee modify Support_Diary varchar(4000)")
# mycursor.execute("ALTER TABLE newtablee modify Resolution varchar(2000)")
# up='''insert into newtablee values (%s)''' %(vari)
# mycursor.executemany(up, val_names)
# mydb.commit()
#
# wb = openpyxl.Workbook()
# sheet = wb.active
# mycursor.execute("select * from newtablee")
# m=2
# for i in mycursor:
#     n=1
#     for j in i:
#         c1 = sheet.cell(row=m, column=n)
#         c1.value=j
#         n+=1
#     m+=1
#
# mycursor.execute("show columns from newtablee")
# m=1
# for i in mycursor:
#     for j in i:
#         c1 = sheet.cell(row=1, column=m)
#         c1.value = j
#         m += 1
#         break
# wb.save("E://updated_v1.xlsx")

from nltk.tokenize import sent_tokenize, word_tokenize
from gensim.test.utils import get_tmpfile
import warnings
import gensim
from gensim.models import Word2Vec, KeyedVectors
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

warnings.filterwarnings(action='ignore')

import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='root', database='test')

mycursor = mydb.cursor()
mycursor.execute("select * from newtablee where row_count=400")
pt = []
for i in mycursor:
    for j in i:
        try:
            j = j.replace(u'\xa0', u' ')
        except:
            pass
        pt.append(j)
# print (pt)
ptt = []
for i in pt:
    if i == pt[0] or i == pt[1] or i == pt[8]:
        x = i
    else:
        x = i.split(" ")
    ptt.append(x)
# print(ptt)
pttt = []
for i in ptt:
    if i == pt[0] or i == pt[1] or i == pt[8]:
        pttt.append(i)
    else:
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

    # print(lstt)


string = pttt
Punctuation(string)

for i in lstt:
    if i == '':
        lstt.remove(i)
# print(lstt)
for i in lstt:
    if i == pt[0] or i == pt[1] or i == pt[8]:
        pttt.append(i)

strr = ''
vip = []
for i in lstt:
    if i == pt[0] or i == pt[1] or i == pt[8]:
        vip.append(i)
    else:
        strr = strr + " " + i

s = " ".join(strr.split())

example_sent = s
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

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
# print(lower_case)

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

# print(lower_cas)
for i in vip:
    lower_cas.append(i)
# print(lower_cas)
lower_ca=[]
for i in lower_cas:
    pattern = re.compile(r'\d[:/]\d[:/]\d\d\d\d')
    matches = pattern.finditer(i)
    count = 0
    for match in matches:
        count += 1
    if count == 0:
        lower_ca.append(i)

final_lst = []
final_lst.append(lower_ca)
print(final_lst)

model = Word2Vec(final_lst, size=1, window=5, min_count=1, workers=4)
word_vectors = model.wv
fname = get_tmpfile("vectors.kv")
# word_vectors.save(fname)
# print(model.predict_output_word(['dsds']))
# print(model.most_similar('issu'))
# tok=['dsds','gsd']
word_vectors = KeyedVectors.load(fname, mmap='r')
# print(KeyedVectors.most_similar_to_given(self=word_vectors, entity1=tok,entities_list=['PriSize Estimation', 'Other Tools', 'AVMCommonPortal_L2']))
print(KeyedVectors.most_similar(self=word_vectors, positive=['sender']))