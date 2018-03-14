# To get columns names use: print(data_c.columns.values)

import pandas as pd
import requests as rq
import json

data=input("Input file name (.csv): ")
code=input("Type your code access:")
output_file_name=input("Type the output file name this way NameYouWant.csv:")

data_c=pd.read_csv(data)
citation_bag=[]
citation_handle=[]
no_citation=[]
no_h_citation=0
h_citation=0

handlesbyjel=data_c['bibliographic.handle'].tolist()

if __name__=="__main__":
    url="https://api.repec.org/call.cgi"
    for handle in handlesbyjel:
        payload = {"code" : code, "getitemcitations" : handle, "repecservice" : "ideas"}
        response = rq.get(url,params=payload)
        if response.status_code==200:
            content = response.content
            if len(content) == 2:
                print ("NO CITATION FOR:", response.url)
                no_citation.append(handle)
                no_h_citation=no_h_citation+1
            else:
                print ("CITATION FOR:", response.url)
                data=json.loads(content)
                x={"cit_handle" : handle}
                data.append(x)
                citation_bag=citation_bag+data
                h_citation=h_citation+1

print("Handles without cites: ",no_h_citation)
print("Handles with cites: ",h_citation)

full_bag=pd.DataFrame(citation_bag)
full_bag=full_bag.fillna(method='bfill')[full_bag.author.notnull()]
full_bag.to_csv("output_file.csv", encoding='utf-8', index=False)
