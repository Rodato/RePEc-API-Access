#This script take the handles that we get with CallsByJEL.py and get the
#reference of each one to make a handles dictionary

import requests as rq
import pandas as pd
import simplejson as sj
import time as time2
import json

bag=[]
no_reponse=[]
counter=0
total_handles=0
handles_answered=0
handles_noanswered=0

input_file_name=input("File name with format (.txt):") #If the handle file was obtained with CallsByJEL.py script, the file format should be txt
code=input("Type your code access:")
output_file_name=input("Type the output file name this way NameYouWant.csv:")
no_response_file=input("Output file name no response handles (.txt):")

f=open(input_file_name,"r+")
lines=f.read().split(',')
lines = [i.replace('"', '') for i in lines]
lines = [i.replace('[', '') for i in lines]
lines = [i.replace(']', '') for i in lines]
handles = [i.replace(' ', '') for i in lines]

if __name__=="__main__":
    url="https://api.repec.org/call.cgi"
    for handle in handles:
        payload = {"code" : code, "getref" : handle, "repecservice" : "ideas"}
        response = rq.get(url,params=payload)
        print ("url call form:", response.url)
        content = response.content
        total_handles=total_handles+1
        if len(content)==0:
            no_response.append(handle)
            handles_noanswered=handles_noanswered+1
        else:
            data=json.loads(content)
            bag=bag+data
            handles_answered=handles_answered+1

        counter=counter+1
        if counter==200:
            print("Sleeping for 120 seconds")
            time2.sleep(120)
            counter=0


full_bag=pd.DataFrame(bag)
full_bag.to_csv(output_file_name, encoding='utf-8', index=False)

if len(no_response)!=0:
    No_R = open(no_response_file, 'w')
    sj.dump(no_response, No_R)
    No_R.close()
    print("Some handles did not have reference information, find it in ", no_response_file)
    print("Handles without reference: ", handles_noanswered)
    print("Handles with reference: ", handles_answered)
else:
    print("All handles had references, find it in ", output_file_name)

print("Total handles: ", total_handles)
print("¡Successful extraction!")
