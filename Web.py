import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import json


file_csv=open('UrlScrapping.csv','w',encoding="utf-8")
file=open('UrlScrapping.json','w',encoding="utf-8")
url="https://egypt.souq.com/eg-ar/iphone/s/?as=1&page="
file.write('[\n')
data={}
csv_column=['name','price','img']

for page in range(1000):
    r=requests.get(url+str(page))
    print("========Page:"+str(page)+"=======")
    soup=BeautifulSoup(r.content,"html.parser")
    anchor=soup.find_all("div",{"class":"column column-block block-list-large single-item"})
    write=csv.DictWriter(file_csv,fieldnames=csv_column)
for pt in anchor:
    name=pt.find('h1',{"class":"itemTitle"})
    price=pt.find('h3',{"class":"itemPrice"})
    img=pt.find('img',{'class':"img-size-medium imageUrl lazy-loaded"})
    if img:
        write.writerow({'name':name.text.replace("            ","").strip("\r\n"),'price':price.text,'img':img.get('src')})
        data["name"]=name.text.replace("            ","").strip("\r\n")
        data["price"]=price.text
        data["img"]=img.text
        json_data=json.dumps(data,ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")
file.write("\n]")
file_csv.close()
file.close()
    



