import pymongo
from pymongo import MongoClient
from twython import TwythonStreamer
from twython import Twython
from textblob import TextBlob
import json

connection=MongoClient()
db=connection['twitterdb1']
collection=db['record_db2']
dict={}
language={}
verification={'true':0,'false':0}
list=[',','(',')',';','!'," "]
for item in collection.find():
    st1=""
    l1=""
    for string in item['description']:
        if(string not in list):
            st1=st1+string
        else:
            #print st1
            if(st1 not in list):
                if(dict.has_key(st1.lower())):
                    val=dict[st1.lower()]
                    del dict[st1.lower()]
                    dict[st1.lower()]=val+1
                else:
                    dict[st1.lower()]=1
            st1=""
    for lang in item['lang']:
        l1=l1+lang
    if(language.has_key(l1.lower())):
        val=language[l1.lower()]
        del language[l1.lower()]
        language[l1.lower()]=val+1
    else:
        language[l1.lower()]=1

    l1=""
    
    if(item['verified']==True):
        verification['true']=verification['true']+1
    elif(item['verified']==False):
        verification['false']=verification['false']+1
 
gender={'male':0,'female':0}
male_list=['male','father','brother','uncle','grandfather','boy','men','man','gentlemen']
female_list=['female','mother','sister','aunt','grandmother','girl','women','woman','lady']
print "We have collected the data of 6100 users for which we were able to calculate the following demographics:"
print "\n\nProfession:\n"


for key,value in dict.items():
    if(key.lower()=="Teacher".lower()):
        print key,value
    elif(key.lower()=="Artist".lower()):
        print key,value
    elif(key.lower()=="Entertainer".lower()):
        print key,value
    elif(key.lower()=="Dancer".lower()):
        print key,value;
    elif(key.lower()=="manager".lower()):
        print key,value
    elif(key.lower()=="Professor".lower()):
        print key,value;
    elif(key.lower()=='Engineer'.lower()):
        print key,value
    elif(key.lower()=="STUDENT".lower()):
        print key,value
    elif(key.lower()=="COMEDIAN".lower()):
        print key,value;
    elif(key.lower()=='ACTOR'.lower()):
        print key,value
    elif(key.lower()=="RESEARCH".lower()):
        print key,value
    elif(key.lower()=="DEVELOPER".lower()):
        print key,value
    elif(key.lower()=="HACKER".lower()):
        print key,value
    elif(key.lower()=="CODER".lower()):
        print key,value;
    elif(key.lower()=="ENTHUSIAST".lower()):
        print key,value
    elif(key.lower()=="PLAYER".lower()):
        print key,value;
    elif(key.lower()=='PRESIDENT'.lower()):
        print key,value
    elif(key.lower()=="CLERK".lower()):
        print key,value
    elif(key.lower()=="OFFICER".lower()):
        print key,value
    elif(key.lower()=="BUSSINESS".lower()):
        print key,value
    elif(key.lower()=="DOCTOR".lower()):
        print key,value;
    elif(key.lower()=="LAWYER".lower()):
        print key,value
    elif(key.lower()=="PHYSICIAN".lower()):
        print key,value;
    elif(key.lower()=='PHARMACIST'.lower()):
        print key,value
    elif(key.lower()=="MECHANIC".lower()):
        print key,value
    elif(key.lower()=="SECRETARY".lower()):
        print key,value
    elif(key.lower()=="DIETICIAN".lower()):
        print key,value
    elif(key.lower()=="ELECTRICIAN".lower()):
        print key,value;
    elif(key.lower()=="SCIENTIST".lower()):
        print key,value
    elif(key.lower()=="ACCOUNTANT".lower()):
        print key,value;
    elif(key.lower()=='CONSULTANT'.lower()):
        print key,value
    elif(key.lower()=='cricketer'):
        print key,value
    elif(key.lower() in male_list):
        temp=gender['male']
        del gender['male']
        gender['male']=temp+value;
    elif(key.lower() in female_list):
        temp=gender['female']
        del gender['female']
        gender['female']=temp+value;
        

print "\n\nGender:\n"
for key,value in gender.items():
    print key,value

print "\n\nVerification:\n"
print "Number Of verified users:", verification['true']
print "Number Of users not verified:", verification['false']

print "\n\nLanguage:\n"
for key,value in language.items():
    if(key=='el'):
        print "Greek",value
    elif(key=='en'):
        print "English",value
    elif(key=='vi'):
        print "Vietnamese",value
    elif(key=='ca'):
        print "Catalan; Valencian",value
    elif(key=='it'):
        print "Italian",value
    elif(key=='eu'):
        print "Basque",value
    elif(key=='ar'):
        print "Arabic",value
    elif(key=='cs'):
        print "Czech",value
    elif(key=='id'):
        print "Indonesian",value
    elif(key=='es'):
        print "Spanish",value
    elif(key=='en-gb'):
        print "English UK",value
    elif(key=='ru'):
        print "Russian",value
    elif(key=='nl'):
        print "Dutch",value
    elif(key=='pt'):
        print "Portuguese",value
    elif(key=='en-au'):
        print "English (Australia)",value
    elif(key=='tr'):
        print "Turkish",value
    elif(key=='zh-cn'):
        print "Chinese (Simplified)",value
    elif(key=='th'):
        print "Thai",value
    elif(key=='ro'):
        print "Romanian",value
    elif(key=='pl'):
        print "Polish",value
    elif(key=='en-gb'):
        print "English UK",value
    elif(key=='fr'):
        print "French",value
    elif(key=='bg'):
        print "Bulgarian",value
    elif(key=='de'):
        print "German",value
    elif(key=='hu'):
        print "Hungarian",value
    elif(key=='hi'):
        print "Hindi",value
    elif(key=='fi'):
        print "Finnish",value
    elif(key=='da'):
        print "Danish",value
    elif(key=='ja'):
        print "Japanese",value
    elif(key=='sr'):
        print "Serbian",value
    elif(key=='no'):
        print "Norwegian",value
    elif(key=='ko'):
        print "Korean",value
    elif(key=='sv'):
        print "Swedish",value
    elif(key=='fil'):
        print "Filipino",value
    elif(key=='zh-tw'):
        print "Chinese (Traditional)",value
    else:
        print key,value

