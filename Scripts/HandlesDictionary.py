#This script take the handles that we get with CallsByJEL.py and get the
#reference of each one to make a handles dictionary

import requests as rq
import pandas as pd
import json

file_name=input("File name with formart (.txt, .json, .csv, etc...):")
code:input("Type your code access:")

f=open(file_name,"r+")

if __name__ == "__main__":
    url="https://api.repec.org/call.cgi"
    for handle in handles:
        payload={"code" : code, "getref" : handle, "repecservice" : "ideas"}
        response = rq.get(url,params=payload)
        print ("url call form:", response.url)
