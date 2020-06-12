
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

warnings.filterwarnings(action='ignore')

import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test')

mycursor=mydb.cursor()
mycursor.execute("select * from newtable where row_count=909")
pt=[]
for i in mycursor:
    for j in i:
        try:
            j = j.replace(u'\xa0', u' ')
        except:
            pass
        pt.append(j)
ptt=[]
for i in pt:
    x=i.split(" ")
    ptt.append(x)

pttt=[]
for i in ptt:
    for j in i:
        pttt.append(j)

lst=[]
lstt=[]

def Punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>'"./?@#$%^&*_~'''
    for i in punctuations:
        lst.append(i)

    for i in pttt:
        if i not in lst:
            lstt.append(i)

    # print (lstt)
string = pttt
Punctuation(string)

for i in lstt:
    if i == '':
        lstt.remove(i)
strr = ''
for i in lstt:
    strr = strr + " " + i

s=" ".join(strr.split())

example_sent =s
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

ls=[]
lss=[]
punctuations = '''!()-[]{};:'"\,<>'"./?@#$%^&*_~'''
for i in punctuations:
    ls.append(i)

for i in filtered_sentence:
    if i not in lst:
        lss.append(i)

ps = PorterStemmer()

words = lss
words_aft_root=[]
for w in words:
    words_aft_root.append(ps.stem(w))

lemmatizer = WordNetLemmatizer()
words_aft_lem=[]
for i in words_aft_root:
    words_aft_lem.append(lemmatizer.lemmatize(i))

lower_case=[]
for i in words_aft_lem:
    lower_case.append(i.lower())
lower_case.pop()
lower_cas=[]
print(lower_case)
import re
for i in lower_case:
    # pattern = re.compile(r'\d[:]\d\d[:]\d\d')
    patterrn = re.compile(r'\d\d[:\]\d\d[:]\d\d')
    # pattern = re.compile(r'\d[/]\d\d[/]\d\d\d\d')
    pattern = re.compile(r'\d[/]\d\d[/]\d\d\d\d')
    matches = pattern.finditer(i)
    count=0
    for match in matches:
        count+=1
    matchees=patterrn.finditer(i)
    count1=0
    for mat in matchees:
        count1+=1
    if i not in lower_cas:
        if count==0:
            if count1==0:
                lower_cas.append(i)
print(lower_cas)
final_lst=[]
final_lst.append(lower_cas)




# 7:17:03
# 12/13/2018


#model1 = gensim.models.Word2Vec(final_lst, min_count=1,size=100, window=5)
#xx=['df','gf','g']
#model1.save('updated.txt')
#print(list(model1.wv.vocab))
#model1=gensim.models.KeyedVectors(final_lst)
#print (model1['refer'])
# model1=gensim.models.KeyedVectors(final_lst)
#model1=Word2Vec.load('thousand.txt')
#model2 = gensim.models.Word2Vec(xx, min_count=1,size=100, window=5)
#model1.train(xx,total_examples=2,epochs=1)
#print(model1.most_similar(positive=['ticket','refer'], negative=['thi']))
#print(model1.most_similar('thi'))
# print(model1)
#print(model1)
# print(model2)
#print(model1.total_train_time)
#print (model1.wv['refer'])
#model2 = gensim.models.Word2Vec(final_lst, min_count=1, size=100, window=5, sg=1)
# print(KeyedVectors.model1.most_similar_to_given('need',['need','mismatch']))
# print(model1.predict_output_word(['inc000032316520', 'applenslite_l2', 'applenslit', 'need', 'clarif', 'timesheet', 'report', 'applen', 'effort', 'mismatch', 'queri', 'keyword', 'adopt', 'fte', 'count', 'issu', 'note', 'vari', 'frequent', 'caus', 'code', 'resolut', 'no', 'due', 'releav', 'join', 'alloc', 'date', 'henc', '694563', '12/31/2018', '11:46:19', 'am', '//', 'harish', 'vijay', '439430', '12/24/2018', '10:41:45', 'meenushre', 'm', '10:41:38', 'in', 'progress', '12/20/2018', '3:27:31', 'pm', '3:18:10', '436569', '12/18/2018', '11:31:34', 'paramasivam', 'krishnamoorthi', '11:31:26', '673898', '11:28:23', 'hi', 'team', 'as', 'check', 'end', '12', 'esa', '2', 'member', 'manag', 'avail', 'altern', 'chang', '11', 'one', 'day', 'next', '12.user', 'want', 'know', 'reason', 'project', 'id:1000224914', 'plea', 'assist', 'user', 'regard', 'avmcoetechdesk', 'subhashini', 's', '11:25:22', '11:25:17', '12/13/2018', '7:39:29', '439435', '7:19:35', 'vishnu', 'priya', 'k', '7:17:03', 'the', 'daili', 'show', 'le', 'number', 'total', 'level', 'calcul', 'i', 'reachabl', '458587/8939705110', 'below', '10', 'aailabl', 'hour', '80', 'ma', '0', 'ticket', '72', 'ar_escal', '1/5/2019', '5:39:38', 'case', 'automat', 'close', '2:01:16', '11:47:20', 'manikandan', 'discus', 'share', 'previou', 'convers', 'if', 'face', 'let', '12/28/2018', '6:02:54', 'remind', 'sent', '12/27/2018', '4:17:41', '1', '12/26/2018', '3:59:37', 'document', 'kindli', 'confirm', '3:58:43', 'attach', 'employe', 'detail', 'find', 'ssonec1697prod', '12/21/2018', '7:12:39', 'could', 'call', 'clarifi', 'would', 'good', 'incid', 'thulasiram', '3:22:59', 'analyz', 'ypur', 'associateid', 'allocationstartd', '281302', '5/1/2018', '330281', '437322', '680449', '257949', '625550', '5/18/2018', '205945', '8/27/2018', '687563', '10/1/2018', '723487', '10/26/2018', '550413', '12/4/2018', '723569', '12/12/2018', '192990', '12/17/2018', 'last', 'list', 'recent', 'so', 'occur', 'mail', 'mention', 'whatev', 'db', 'gener', '12/19/2018', '8:06:51', 'we', 'get', 'solut', '10:45:33', 'ani', 'updat', 'request..', '6:21:34', '9:40:45', '7:43:46', 'dear', 'thank', 'reach', 'thi', 'refer', 'request', 'gokulfg', 'inform', 'tomorrow', "'s", 'u', 'gsd', 'contact', 'c2', 'other']))
print('cool')


# print(model2.predict_output_word(['vfg','mkj']))