#This script take the handles that we get with CallsByJEL.py and get the
#reference of each one to make a handles dictionary

import requests as rq
import pandas as pd
import json

bag=[]
output_file_name=input("Type the output file name this way NameYouWant.csv:")

input_file_name=input("File name with format (.txt):") #If the handle file was obtained with CallsByJEL.py script, the file format should be txt
code:input("Type your code access:")

f=open(input_file_name,"r+")
lines=f.read().split(',')
lines = [i.replace('"', '') for i in lines]
lines = [i.replace('[', '') for i in lines]
lines = [i.replace(']', '') for i in lines]
lines = [i.replace(' ', '') for i in lines]

if __name__ == "__main__":
    url="https://api.repec.org/call.cgi"
    for handle in handles:
        payload={"code" : code, "getref" : handle, "repecservice" : "ideas"}
        response = rq.get(url,params=payload)
        print ("url call form:", response.url)
        content= response.content
        data=json.loads(content)
        bag=bag+data


full_bag=pd.DataFrame(bag)
full_bag.to_csv(output_file_name, encoding='utf-8', index=False)
