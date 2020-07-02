import os
import sys
import urllib.request
import csv
import json
import re

client_id = "53nIyFKGsh8M8WtV8EWj"
client_secret = "5ikblQCDKT"
encText = urllib.parse.quote("남자")
url = "https://openapi.naver.com/v1/search/blog?query="+encText+"$display=100"# json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request) #urlopen을 통해서 응답을 받는 다 
rescode = response.getcode() # urlopen().getcode() : HTTP 응답 코드를 정수로 반환( 200, 404 ) 왜쓰는 지는 ?
                            #에러 처리를 받기 위한 함수 just like try exception

jsondata=[]
#jsondata[0] = 딕셔너리 접근 가능하다 왜냐면 [{key:value}] 이렇게 저장되어 있으니까

if(rescode==200): #서버가 요청을 제대로 처리 했음
    response_json = json.load(response)
    jsondata.append(response_json)
    
    with open('navernews/test_title3.json', 'w', encoding='utf-8') as make_file:
        json.dump(response_json, make_file, indent="\t",ensure_ascii=False)

        for i in range(0,10):
            title = jsondata[0]["items"][i]["title"]
            #print(title)
            title = re.sub("(<([^>]+)>)",'',title,0,re.I|re.S)
            print(title)
   
else:
    print("Error Code:" + rescode)
