#In this program we get all the RePEc articles handles by JEL code.


import requests as rq
import json

All_Data=list()

code=input("Type your code access:")
offset=input("offset:")
offset=int(offset)
JEL=input("JEL code:")


if __name__ == "__main__":
    url="https://api.repec.org/call.cgi"
    payload={"code" : code, "offset" : offset, "getrecentjel" : JEL, "repecservice" : "ideas"}
    response = rq.get(url,params=payload)
    print ("url call form:", response.url)

    if response.status_code==200:
        print("Right Call")
        content = response.content
        if len(content)!=0:
            print("Storing data")
            All_Data=All_Data+content
            print("Updating call...")
            payload["offset"]=payload["offset"]+25
            print("Solicitude:", payload["offset"])
            response = rq.get(url,params=payload)
            print ("url call form:", response.url)
            content = response.content
        else:
            datos=open("Handles_by_JEL.json","wb")
            datos.write(All_Data)
            datos.close()
    else:
        print("Status:", response, "please, verify your access code or url call form")

print("¡All the data collected!")
