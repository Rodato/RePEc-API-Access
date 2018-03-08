#This script take the handles that we get with CallsByJEL.py and get the
#reference of each one to make a handles dictionary

import requests as rq
import pandas as pd
import json

bag=[]
no_reponse=[]
counter=0

input_file_name=input("File name with format (.txt):") #If the handle file was obtained with CallsByJEL.py script, the file format should be txt
code:input("Type your code access:")
output_file_name=input("Type the output file name this way NameYouWant.csv:")
no_response_file=inpur("Output file name no response handles (.txt):")

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
        if len(content)==0:
            no_response.append(handle)
        else:
            data=json.loads(content)
            bag=bag+data
            counter=counter+1
            if counter==200:
                time.sleep(120)
                counter=0
                print("Sleeping for 120 seconds")


full_bag=pd.DataFrame(bag)
full_bag.to_csv(output_file_name, encoding='utf-8', index=False)

if len(no_response)!=0:
    No_R = open(no_response_file, 'w')
    sj.dump(no_response, No_R)
    No_R.close()
    print("Some hanldes did not have reference information, find it in ", no_response_file)
else:
    print("All handles had referencesm find it in ", output_file_name)

print("¡Successful extraction!")
