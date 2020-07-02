import os
import sys
import urllib.request
import csv
import json
import re

client_id = "53nIyFKGsh8M8WtV8EWj"
client_secret = "5ikblQCDKT"
encText = urllib.parse.quote("여행")
url = "https://openapi.naver.com/v1/search/blog?query="+encText+"$display=100"# json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

jsondata=[]
#jsondata[0] = 딕셔너리 접근 가능하다 왜냐면 [{key:value}] 이렇게 저장되어 있으니까

if(rescode==200):
    response_json = json.load(response)
    jsondata.append(response_json)
    
    with open('navernews/test_title2.json', 'w', encoding='utf-8') as make_file:
        json.dump(response_json, make_file, indent="\t",ensure_ascii=False)

        for i in range(0,10):
            title = jsondata[0]["items"][i]["title"]
            #print(title)
            title = re.sub("(<([^>]+)>)",'',title,0,re.I|re.S)
            print(title)
   
else:
    print("Error Code:" + rescode)

