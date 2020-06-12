import mysql.connector
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# warnings.filterwarnings(action='ignore')
#
# mydb=mysql.connector.connect(host='localhost',user='root',passwd='root',database='test')
#
# final_lst=[]
# for iii in range(1,999):
#     mycursor = mydb.cursor()
#     sql="select * from qwerty where row_count=(%s)"
#     form=(iii,)
#     mycursor.execute(sql,form)
#     pt = []
#     for i in mycursor:
#         for j in i:
#             try:
#                 j = j.replace(u'\xa0', u' ')
#             except:
#                 pass
#             pt.append(j)
#     ptt = []
#     for i in pt:
#         x = i.split(" ")
#         ptt.append(x)
#
#     pttt = []
#     for i in ptt:
#         for j in i:
#             pttt.append(j)
#
#     lst = []
#     lstt = []
#
#
#     def Punctuation(string):
#         punctuations = '''!()-[]{};:'"\,<>'"./?@#$%^&*_~'''
#         for i in punctuations:
#             lst.append(i)
#
#         for i in pttt:
#             if i not in lst:
#                 lstt.append(i)
#
#         # print (lstt)
#
#
#     string = pttt
#     Punctuation(string)
#
#     for i in lstt:
#         if i == '':
#             lstt.remove(i)
#     strr = ''
#     for i in lstt:
#         strr = strr + " " + i
#
#     s = " ".join(strr.split())
#
#     example_sent = s
#     stop_words = set(stopwords.words('english'))
#
#     word_tokens = word_tokenize(example_sent)
#
#     filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
#     filtered_sentence = []
#
#     for w in word_tokens:
#         if w not in stop_words:
#             filtered_sentence.append(w)
#
#     ls = []
#     lss = []
#     punctuations = '''!()-[]{};:'"\,<>'"./?@#$%^&*_~'''
#     for i in punctuations:
#         ls.append(i)
#
#     for i in filtered_sentence:
#         if i not in lst:
#             lss.append(i)
#
#     ps = PorterStemmer()
#
#     words = lss
#     words_aft_root = []
#     for w in words:
#         words_aft_root.append(ps.stem(w))
#
#     lemmatizer = WordNetLemmatizer()
#     words_aft_lem = []
#     for i in words_aft_root:
#         words_aft_lem.append(lemmatizer.lemmatize(i))
#
#     lower_case = []
#     for i in words_aft_lem:
#         lower_case.append(i.lower())
#     lower_case.pop()
#     lower_cas = []
#     #print(lower_case)
#     for i in lower_case:
#         if i not in lower_cas:
#             lower_cas.append(i)
#     #print(lower_cas)
#     final_lst.append(lower_case)
# model2 = gensim.models.Word2Vec(final_lst, min_count=5,size=100, window=5)
# model1.save('thousand.txt')
v=['inc000032235968', '673898', 'l1', 'avm', 'tool', 'portal', 'applenslit', 'report', 'need', 'access', 'qliksens', 'it', 'servic', 'india', 'ssh0243', 'rsa', 'ins-rsa', 'commit', 'uae-', 'user', 'request', 'insur', 'success', 'emc', 'is', 'standard', 'qlik', 'sen', 'dl', 'dear', 'kailash', 'thank', 'reach', 'avmcoetechdesk', 'thi', 'refer', 'ticket', 'number', 'we', 'understand', 'descript', 'resolut', 'plea', 'inform', 'provided.request', 'yoju', 'check', 'revert', 'back', 'issu', 'contact', 'u', 'http', '//gsd.cognizant.com', 'clarif', 'regard', '12/12/2018', '2:02:34', 'pm', 'in', 'progress', 'subhashini', 's', '12/11/2018', '7:46:19', '674096', '7:45:20', 'rameezh', 'ka', '623201', '7:25:00', 'hi', 'team', 'applen', 'download', 'kindli', 'app', 'support', 'sree', 'vignesh', '680068', '7:15:08', 'not', 'scope', 'as', 'discus', 'face', 'get', 'len', 'henc', 'transfer', '1c', '6:45:38', 'jagadesan', 'viswanathan', 'approv', '7:01:54', 'apac', '1c-l1', 'afzal', 'khan', 'b', '6:41:30', 'middl', 'east', 'ltd', 'ec', 'add', 'i', 'could', 'abl', 'download/view', 'time', 'sheet', '2:03:23', '9:36:17', 'mail', 'concern', 'access.wil', 'udat', 'provid', 'sinnochamp', '7:20:54', 'applic', 'our', 'engin', 'start', 'work', 'share', 'updat', 'soon', 'possibl', 'shall', 'addit', 'requir', 'innochamp', '7:20:53', 'your', 'assign', 'one', 'member', '6:29:08', 'murthi', 'rais', 'op', 'either', 'ping', 'call', 'you', 'distribut', 'list', 'modifi', 'renam', '1capp']
model1=Word2Vec.load('thousand.txt')
print(model1.predict_output_word(v))
print()
# print(model1.most_similar('672849'))
# print(model1.corpus_total_words)
# print(model1.corpus_count)
#print(model1.reset_from())


# model_2=Word2Vec(size=300, min_count=1)
# model_2.build_vocab(v)
# model_2.train(['h'], total_examples=1, epochs=1)
# print(model_2.model_trimmed_post_training)