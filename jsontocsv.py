import csv
import json

input_file_name = "sample/PBDS.csv"
output_file_name = "sample/json.txt"
#with open(input_file_name, "r", encoding="utf-8", newline="") as input_file, \
#        open(output_file_name, "w", encoding="utf-8", newline="") as output_file:

input_file = open(input_file_name, "r", encoding="utf-8", newline="")
output_file = open(output_file_name, "w", encoding="utf-8", newline="")

reader = csv.reader(input_file)
#첫 줄은 col_names 리스트로 읽어 놓고 한위에 한 줄을 읽어서 col_names에 스트링 형태로 저장한다.
col_names = next(reader) #리스트형태로 저장된다.
#next는 첫재줄을 쓰고 버리고 다음줄부터 시작한다.
#그 다음 줄부터 zip으로 묶어서 json으로 dumps

for cols in reader:
    doc = {
        col_name: col for col_name, col in zip(col_names, cols)}#zip은 튜플형태로 묶어준다
     
    print(json.dumps(doc, ensure_ascii=False), file=output_file)
    #ascii 쓰지 않는다는 내용.
    #doc에 넣어주고 
    #문자열을 던져 주고 있다 key형태로(json.dumps)
    #print 로 받아주는 것이다