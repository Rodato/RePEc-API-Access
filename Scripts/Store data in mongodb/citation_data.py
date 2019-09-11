import requests
from pymongo import MongoClient
import json
from ast import literal_eval
import time as time2

path=""
i_f_n=input("Input file name without format:")
input_file_name=path+"/"+i_f_n+".txt"
f=open(input_file_name,"r")

handles = f.read().split(',')
handles = [i.replace('"', '') for i in handles]
handles = [i.replace('[', '') for i in handles]
handles = [i.replace(']', '') for i in handles]
handles = [i.replace(' ', '') for i in handles]

data=[]

print("total solicitudes ", len(handles))

n1=input("First solicitude number:")
n1=int(n1)
n2=input("Second solicitude number:")
n2=int(n2)
handles=handles[n1:n2]

print("total solicitudes ", n2-1)


url="https://api.repec.org/call.cgi"

#Create connection to MongoDB
client = MongoClient("localhost", 27017)
db = client[""] #db name here
coll=i_f_n #the collection name is like the input file name
collection = db[coll]

for handle in handles:
    payload = {"code" : "", "getitemcitations" : handle, "repecservice" : "ideas"}
    response = requests.get(url,params=payload)
    print ("url call form: ", response.url)
    if response.status_code==200:
        paper_info = response.text
        d=json.loads(paper_info)
        if len(d)>0:
            for cit_info in d:
                cit_info["cit_handle"]=handle
            collection.insert(cit_info,check_keys=False)
        else:
            print("No Data")
    else:
        print("NO DATA for ", handle)


print(' *** DONE *** ')
