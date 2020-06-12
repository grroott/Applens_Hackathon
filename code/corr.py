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

for iii in range(101, 105):
    mycursor = mydb.cursor()
    # sql = "select Item,Summary,Resolution,Support_Diary,Notes,Work_Log from newtablee where row_count=(%s)"
    # form = (iii,)
    # mycursor.execute(sql, form)
    strr = ''
    lst = []
    # for i in mycursor:
    #     for j in i:
    #         strr = strr + j
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
print(final_lst)

# final_lst=[[' L1 (AVM Tools & Portals) AppLensLite', 'AppLensLite'], [' AVMPMO_L2 AVM PMO', 'AVM PMO'], [' AVMPMO_L2 AVM PMO', 'AVM PMO'], [' L1 (AVM Tools & Portals) AppLensLite', 'AppLensLite']]

'''final_lst=[["Reports issue in AVM PMOAVM PMO - Reports issue in AVM PMONone597603 1/14/2019 4:10:14 PM\xa0\xa0WIP\xa0\xa0SRI RAM\xa0\xa0\xa0\xa0625820 1/14/2019 4:05:59 PM\xa0\xa0Hi\xa0\xa0Team,\xa0\xa0Please change the status of the SO 30989171\xa0\xa0to '1.2 Pending Demand Validation'\xa0\xa0Regards AVMTechdesk\xa0\xa0Keerthana G S\xa0\xa0\xa0Please change the status of the SO 30989171\xa0\xa0to '1.2 Pending Demand Validation'597603 1/14/2019 4:11:21 PM\xa0\xa0\xa0status of the SO 30989171 updated to '1.2 Pending Demand Validation'\xa0\xa0SRI RAM\xa0\xa0\xa0 AVMPMO_L2 AVM PMO"],
['Unable to view the Account name in the drop downUnable to view the Account name in the drop down in AppLensDear Dineshraja ,\xa0\xa0Thank for reaching AVMCoETechDesk.\xa0\xa0This is reference to the Ticket Number: INC000033486961\xa0\xa0Request:\xa0\xa0We understand from your description that,Unable to view the Account name in the drop down in AppLens\xa0\xa0\xa0Resolution:\xa0\xa0Please be informed that,As discussed in skype, 1000226512 this project was not onboarded to applens. kindly navigate to https://applens.cognizant.com\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Regards, AVMCoETechDesk.675017 1/14/2019 12:49:51 PM\xa0\xa0//\xa0\xa0Dhilip Kumar\xa0\xa0\xa0\xa0675017 1/14/2019 12:29:13 PM\xa0\xa0//\xa0\xa0Dhilip Kumar\xa0\xa0\xa0\xa0625820 1/14/2019 11:48:38 AM\xa0\xa0Progress\xa0\xa0Keerthana G S\xa0\xa0\xa0\xa0437595 1/14/2019 9:32:19 AM\xa0\xa0Wip\xa0\xa0Vijayalakshmi A\xa0\xa0\xa0\xa0673898 1/11/2019 5:19:15 PM\xa0\xa0a\xa0\xa0Subhashini S\xa0\xa0\xa0I am part of two projects in two different accounts. I am not able to see the other account in Applens. Please help. Previous refernce - INC000029009799\xa0\xa0Thanks, Dinesh675017 1/14/2019 12:52:46 PM\xa0\xa0Dear Dineshraja ,\xa0\xa0Thank for reaching AVMCoETechDesk.\xa0\xa0This is reference to the Ticket Number: INC000033486961\xa0\xa0Request:\xa0\xa0We understand from your description that,Unable to view the Account name in the drop down in AppLens\xa0\xa0\xa0Resolution:\xa0\xa0Please be informed that,As discussed in skype, 1000226512 this project was not onboarded to applens. kindly navigate to https://applens.cognizant.com\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Regards, AVMCoETechDesk.\xa0\xa0Dhilip Kumar\xa0\xa0\xa0\xa01CAPP 1/14/2019 11:48:09 AM\xa0\xa0i am allocated to one account and also the esa pm of another account as specified earlier. can you please advise further? i am available between 12 – 9 ist today.\xa0\xa0Dineshraja K Venkatesan\xa0\xa0\xa0\xa0675017 1/14/2019 10:08:05 AM\xa0\xa0Dear Dineshraja ,\xa0\xa0Thank for reaching AVMCoETechDesk.\xa0\xa0This is reference to the Ticket Number: INC000033486961\xa0\xa0Request:\xa0\xa0We understand from your description that,Unable to view the Account name in the drop down in AppLens\xa0\xa0\xa0Resolution:\xa0\xa0Please be informed that,As we try to reach you through skype , but you are not available. As checked from our end ,you were allocated to the project -1000196292,hence you were able to view only 1 account in AppLens.\xa0\xa0Please note,if you are allocated in another project also,please share us the screenshot of the allocated project to check from our end.\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Regards, AVMCoETechDesk.\xa0\xa0Dhilip Kumar\xa0\xa0\xa0\xa0SSOneC1697PROD 1/13/2019 6:53:36 PM\xa0\xa0Hi Team, I am allocated to BT allium but also the ESA PM for the project Project\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0:1000226512 Project Name\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0:News Am-NAM Managed Services-M. This is not visible in Applens. Please help.\xa0\xa0Dineshraja K Venkatesan\xa0\xa0\xa0\xa01CAPP 1/13/2019 6:38:06 PM\xa0\xa0hi team, i am allocated to bt allium but also the esa pm for the project project\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0:1000226512 project name\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0:news am-nam managed services-m. this is not visible in applens. please help.\xa0\xa0Dineshraja K Venkatesan\xa0\xa0\xa0\xa0673898 1/11/2019 7:04:11 PM\xa0\xa0Dear Dineshraja ,\xa0\xa0Thank for reaching AVMCoETechDesk.\xa0\xa0This is reference to the Ticket Number: INC000033486961\xa0\xa0Request:\xa0\xa0We understand from your description that,Unable to view the Account name in the drop down in AppLens\xa0\xa0\xa0Resolution:\xa0\xa0Please be informed that, as checked from our end ,you were allocated to the project -1000196292,hence you were able to view only 1 account in AppLens.\xa0\xa0Please note,if you are allocated in another project also,please share us the screenshot of the allocated project to check from our end.\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Regards, AVMCoETechDesk.\xa0\xa0\xa0\xa0\xa0\xa0Subhashini S\xa0\xa0\xa0 L1 (AVM Tools & Portals) AppLens'],
['How to unfreeze timesheetUnable to unfreeze the DART timesheet for holidayHi Vignesh,\xa0\xa0Thank you for contacting AVMCoETechDesk.\xa0\xa0This is with reference to the Ticket number: "INC000033484160"\xa0\xa0Issue Description: Facing issues in App Lens Approve/unfreeze screen\xa0\xa0Information Provided:\xa0\xa0\xa0As discussed on Skype, please be informed that we request you to select the date from calendar picker and unfreeze/approve the timesheet since we are facing issues in graph and when you click on graph, it will show 2018 data.\xa0\xa0Our technical team is working on the same and will be fixed at earliest.\xa0\xa0We are resolving this case from our end.\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Warm Regards, AVMCoETechDesk.439435 1/11/2019 4:11:51 PM\xa0\xa0In Progress\xa0\xa0Vishnu Priya K\xa0\xa0\xa0\xa0673898 1/11/2019 4:05:07 PM\xa0\xa0a\xa0\xa0Subhashini S\xa0\xa0\xa0Unable to unfreeze at applens starting from 2nd January439435 1/11/2019 4:26:42 PM\xa0\xa0Hi Vignesh,\xa0\xa0Thank you for contacting AVMCoETechDesk.\xa0\xa0This is with reference to the Ticket number: "INC000033484160"\xa0\xa0Issue Description: Facing issues in App Lens Approve/unfreeze screen\xa0\xa0Information Provided:\xa0\xa0\xa0As discussed on Skype, please be informed that we request you to select the date from calendar picker and unfreeze/approve the timesheet since we are facing issues in graph and when you click on graph, it will show 2018 data.\xa0\xa0Our technical team is working on the same and will be fixed at earliest.\xa0\xa0We are resolving this case from our end.\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Warm Regards, AVMCoETechDesk.\xa0\xa0Vishnu Priya K\xa0\xa0\xa0\xa0 L1 (AVM Tools & Portals) AppLensLite'],
['Queries on Debt configurationClarification on DD template for Debt managementDear Banu ,\xa0\xa0Thank for reaching AVMCoETechDesk.\xa0\xa0This is reference to the Ticket Number: INC000033482924\xa0\xa0Request:\xa0\xa0We understand from your description that, Clarification on DD template for Debt management\xa0\xa0Resolution:\xa0\xa0Please be informed that, as discussed on call,the cause code is mandatory for debt in AppLens.\xa0\xa0Request you to download the template and provide the required fields and upload the same.\xa0\xa0The users will be able to view the debt mandatory fields while closing the ticket and they have to select the cause code and resolution code manually from drop down.\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Regards, AVMCoETechDesk.625820 1/11/2019 3:49:57 PM\xa0\xa0In Progress\xa0\xa0Keerthana G S\xa0\xa0\xa0For Debt Management enablement, in DD template cause code will be automatically mapped or manually to be selected by analysts673898 1/11/2019 4:52:31 PM\xa0\xa0Dear Banu ,\xa0\xa0Thank for reaching AVMCoETechDesk.\xa0\xa0This is reference to the Ticket Number: INC000033482924\xa0\xa0Request:\xa0\xa0We understand from your description that, Clarification on DD template for Debt management\xa0\xa0Resolution:\xa0\xa0Please be informed that, as discussed on call,the cause code is mandatory for debt in AppLens.\xa0\xa0Request you to download the template and provide the required fields and upload the same.\xa0\xa0The users will be able to view the debt mandatory fields while closing the ticket and they have to select the cause code and resolution code manually from drop down.\xa0\xa0Please contact us through https://gsd.cognizant.com for any further clarifications.\xa0\xa0Regards, AVMCoETechDesk.\xa0\xa0\xa0\xa0\xa0\xa0Subhashini S\xa0\xa0\xa0 L1 (AVM Tools & Portals) AppLensLite']
]'''
print(type(final_lst))
final_lst = pd.DataFrame(final_lst)
final_lst.columns = ["Details"]
# nltk.download('stopwords')
corpus = []
for i in range(0, 4):
    text = re.sub('[^a-zA-Z]', '', final_lst['Details'][i])
    text = text.lower()
    text = text.split()
    ps = PorterStemmer()
    text = ''.join(text)
    corpus.append(text)
# creating bag of words model
cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()
# fitting naive bayes to the training set
f = open('my_classifier1.pickle', 'rb')
classifier = pickle.load(f)
print(classifier.predict(X))
f.close()





