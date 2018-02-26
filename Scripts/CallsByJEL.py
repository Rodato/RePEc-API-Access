import requests as rq
import json
#from bs4 import BeautifulSoup

#JEL=["E1","E2","E3","E4","E5","E6","E7"]
All_Data=list()
offset=input("offset:")
offset=int(offset)
code=input("Type your code access:")
if __name__ == "__main__":
    url="https://api.repec.org/call.cgi"
    payload={"code" : code, "offset" : offset, "getrecentjel" : "E1", "repecservice" : "ideas"}
    response = rq.get(url,params=payload)
    print ("url call form:", response.url)

    if response.status_code==200:
        print("Petición correcta")
        content = response.content
        if len(content)!=0:
            print("Almacenando datos")
            All_Data=All_Data+content
            print("Actualizando petición...")
            payload["offset"]=payload["offset"]+25
            print("Solicitud:", payload["offset"])
            response = rq.get(url,params=payload)
            print ("url call form:", response.url)
            content = response.content
        else:
            datos=open("Handles_by_JEL.json","wb")
            datos.write(All_Data)
            datos.close()
    else:
        print("Status:", response, "por favor verificar")

print("¡Extracción Completa!")
