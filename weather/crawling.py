# https://www.weather.go.kr/weather/climate/past_cal.jsp?stn=108&yy=2020&mm=6&obs=1&x=28&y=3

import requests #특수변수 혹은 모듈이라고 불리는 놈 to send HTTP requests using Python. 즉 HTTP requests를 보낸다고 한다.
import calendar #특수변수 혹은 모듈이라고 불리는 놈 날짜관련
import datetime #특수변수 혹은 모듈이라고 불리는 놈 시간관련
from bs4 import BeautifulSoup #특수변수 혹은 모듈이라고 불리는 놈인데 웹 데이터 크롤링 또는 스크래핑을 할 때 사용하

data = [] #data 리스트안에 저장할 장소 생성
now = datetime.datetime.now() #now변수에 지금 시간을 저장
y = now.strftime('%Y') #연도 #y변수에 지금 시간과 년도 저장
m = now.strftime('%m') #월 #x변수에 지금 시간과 월 저장
response = requests.get( #겟 방식으로 연도 자리 y들어가고 월자리에 y 들어간다.
    'http://www.kma.go.kr/weather/climate/past_cal.jsp?stn=108&yy='+str(y)+'&mm='+str(m)+'&obs=1') #끝에 obs=1는 뭐지?
soup = BeautifulSoup(response.content, 'html.parser') #아마도 저 url을 열어주는 기능이 아닐까싶다.
table = soup.find('table', {'class': 'table_develop'}) #함수 인자로는 찾고자 하는 태그의 이름, 속성 기타 등등이 들어간다
                                                    #즉 table에 class key값에 table_develop 이라는 value값은 찾는다.

#컨트롤 변수들
count = 0
point = [''] * 7
pointt = [''] * 7
fstr = [''] * 7
tstr = [''] * 7
mstr = [''] * 7
estr = [''] * 7
temp = [''] * 7
temptop = [''] * 7
tempmin = [''] * 7
rain = [''] * 7

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))

    if tds:
        for i in range(0, 7):
            point[i] = tds[i].text

        if count % 2 != 0:
            for j in range(0, 7):
                pointt[j] = point[j].translate({ord('일'): ''}) #트랜스레이트 한다는 것인데 ord('일')는 문자의 아스키 코드 값을 돌려주는 함수이다.
                                                                #※ ord 함수는 chr 함수와 반대이다.

        if count % 2 == 0:
            for k in range(0, 7):
                fstr[k] = point[k].find('최고기온')
                tstr[k] = point[k].find('최저기온')
                mstr[k] = point[k].find('평균운량')
                estr[k] = point[k].find('일강수량')
                temp[k] = point[k][5:fstr[k]].translate({ord('℃'): ''})
                temptop[k] = point[k][fstr[k]+5:tstr[k]
                                      ].translate({ord('℃'): ''})
                tempmin[k] = point[k][tstr[k]+5:mstr[k]
                                      ].translate({ord('℃'): ''})
                rain[k] = point[k][estr[k] +
                                   5:].translate({ord(' '): '', ord('-'): '0.0', ord('m'): ''})

            if pointt[0] == '\xa0' or temp[0] == '':
                sun = ""
            else:
                sun = str(
                    y)+'-'+str(m)+'-'+pointt[0]+' '+temp[0]+' '+temptop[0]+' '+tempmin[0]+' '+rain[0]
                data.append([sun])

            if pointt[1] == '\xa0' or temp[1] == '':
                mon = ""
            else:
                mon = str(
                    y)+'-'+str(m)+'-'+pointt[1]+' '+temp[1]+' '+temptop[1]+' '+tempmin[1]+' '+rain[1]
                data.append([mon])

            if pointt[2] == '\xa0' or temp[2] == '':
                tue = ""
            else:
                tue = str(
                    y)+'-'+str(m)+'-'+pointt[2]+' '+temp[2]+' '+temptop[2]+' '+tempmin[2]+' '+rain[2]
                data.append([tue])

            if pointt[3] == '\xa0' or temp[3] == '':
                wed = ""
            else:
                wed = str(
                    y)+'-'+str(m)+'-'+pointt[3]+' '+temp[3]+' '+temptop[3]+' '+tempmin[3]+' '+rain[3]
                data.append([wed])

            if pointt[4] == '\xa0' or temp[4] == '':
                thu = ""
            else:
                thu = str(
                    y)+'-'+str(m)+'-'+pointt[4]+' '+temp[4]+' '+temptop[4]+' '+tempmin[4]+' '+rain[4]
                data.append([thu])

            if pointt[5] == '\xa0' or temp[5] == '':
                fri = ""
            else:
                fri = str(
                    y)+'-'+str(m)+'-'+pointt[5]+' '+temp[5]+' '+temptop[5]+' '+tempmin[5]+' '+rain[5]
                data.append([fri])

            if pointt[6] == '\xa0' or temp[6] == '':
                sat = ""
            else:
                sat = str(
                    y)+'-'+str(m)+'-'+pointt[6]+' '+temp[6]+' '+temptop[6]+' '+tempmin[6]+' '+rain[6]
                data.append([sat])

            print(sun)
            print(mon)
            print(tue)
            print(wed)
            print(thu)
            print(fri)
            print(sat)
    count += 1

with open('weather/weather.txt', 'w') as file:
    for i in data:
        file.write('{0}\n'.format(i[0]))
