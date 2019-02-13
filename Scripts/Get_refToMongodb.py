import requests
from pymongo import MongoClient
import json
from ast import literal_eval
import time as time2

i_f_n=input("Input file name without formart (.txt)):")
input_file_name=i_f_n+".txt"

f=open(input_file_name,"r")

lines=f.read().split(',')
lines = [i.replace('"', '') for i in lines]
lines = [i.replace('[', '') for i in lines]
lines = [i.replace(']', '') for i in lines]
handles = [i.replace(' ', '') for i in lines]

data=[]
counter=0
solicitude=0

print("total solicitudes a hacer ", len(handles))

#Get the data into a list
url="https://api.repec.org/call.cgi"
for handle in handles:
    payload = {"code" : "Y3f18KM3", "getref" : handle, "repecservice" : "ideas"}
    response = requests.get(url,params=payload)
    paper_info = response.text
    solicitude=solicitude+1
    if len(paper_info)>0:
        data.append(paper_info)
        print(" [*] Data collected", solicitude)
    else:
        print(" [*] Data collected", solicitude, "NO ANSWERD")

    counter=counter+1
    if counter==200:
        print("Sleeping for 120 seconds")
        time2.sleep(120)
        counter=0

# Create connection to MongoDB
client = MongoClient('localhost', 27017)
db = client['EcoEmp_db']
collection = db[i_f_n]

for i in data:
    d=json.loads(i)
    collection.insert(d)

print(' *** DONE *** ')
