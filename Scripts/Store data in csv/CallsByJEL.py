#In this program we get all the RePEc articles handles by JEL code.

import requests as rq
import simplejson as sj

All_handles=list()

code=input("Type your access code:")
offset=input("offset:")
offset=int(offset)
JEL=input("JEL code:")
output_file_name=input("Output file name (NameYouWant.txt):")


if __name__ == "__main__":
    url="https://api.repec.org/call.cgi"
    payload={"code" : code, "offset" : offset, "getrecentjel" : JEL, "repecservice" : "ideas"}
    response = rq.get(url,params=payload)
    print ("url call form:", response.url)

    if response.status_code==200:
        print("Right call")
        content = response.content
        first_data=content.decode("utf-8")
        y=first_data.replace("[", "")
        y=y.replace("]", "")
        y=y.split(",")
        y=[i.replace('"', '') for i in y]
        while payload["offset"]<9999999999: #This is a default value
            print("Storing data")
            All_handles=All_handles+y
            print("Updating offset call...")
            payload["offset"]=payload["offset"]+25
            print("New offset value:", payload["offset"])
            response = rq.get(url,params=payload)
            print ("url call form:", response.url)
            content = response.content
            first_data=content.decode("utf-8")
            if first_data=='[{"error":43}]': # [{"error":43}] is the API answer when the call does not have data
                break
            y=first_data.replace("[", "")
            y=y.replace("]", "")
            y=y.split(",")
            y=[i.replace('"', '') for i in y]
    else:
        print("Wrong call")
        print(response.status_code, "verify this code in requests web site: http://docs.python-requests.org/en/master/")

f = open(output_file_name, 'w')
sj.dump(All_handles, f)
f.close()

print("¡All data was obtained!")
