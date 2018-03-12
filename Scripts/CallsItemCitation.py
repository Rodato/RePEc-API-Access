import pandas as pd
import requests
import json

data=input("Input file name (.csv): ")
code:input("Type your code access:")
output_file_name=input("Type the output file name this way NameYouWant.csv:")

data_c=pd.read_csv(data)

#print(data_c.columns.values) #Get the columns names

handlesbyjel=data_c['bibliographic.handle'].tolist()

if __name__=="__main__":
    url="https://api.repec.org/call.cgi"
    for handle in handlesbyjel:
        payload = {"code" : code, "getitemcitation" : handle, "repecservice" : "ideas"}
