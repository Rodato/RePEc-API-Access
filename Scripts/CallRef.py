import requests as rq
import pandas as pd
import time as time2
import simplejson as sj
import json

bag=[]
counter=0

input_file_name=input("Input file name with formart (.txt)):")
output_file_name=input("Output file name with csv formart:")

f=open(input_file_name,"r")

lines=f.read().split(',')
lines = [i.replace('"', '') for i in lines]
lines = [i.replace('[', '') for i in lines]
lines = [i.replace(']', '') for i in lines]
handles = [i.replace(' ', '') for i in lines]

if __name__=="__main__":
    url="https://api.repec.org/call.cgi"
    for handle in handles:
        payload = {"code" : "RL2qVaps", "getref" : handle, "repecservice" : "ideas"}
        response = rq.get(url,params=payload)
        print ("url call form:", response.url)
        content = response.content
        if len(content)==0:
            no_response.append(handle)
        else:
            data=json.loads(content)
            bag=bag+data
            
        counter=counter+1
        if counter==200:
            print("Sleeping for 120 seconds")
            time2.sleep(120)
            counter=0


full_bag=pd.DataFrame(bag)
full_bag.to_csv(output_file_name, encoding='utf-8', index=False)

print("Proceso completado")
