import csv
import json

input_file_name = "sample/json.txt" #json은 기본적으로 딕셔너리 형태로 있는 것이다
output_file_name = "sample/test.csv" 

input_file = open(input_file_name, "r", encoding="utf-8", newline="")
output_file = open(output_file_name, "w", encoding="utf-8", newline="")


data = []
for line in input_file:
    datum = json.loads(line) #값을 던져 주었을 때 딕셔너리화 된다.
    data.append(datum)

csvwriter = csv.writer(output_file)#파일 객체를 csv 로 만들어서 csvwriter에 던져 주는 것이다
csvwriter.writerow(data[0].keys())#라인으로 한줄한줄 쓴다 그래서 write row이다.
for line in data:
    csvwriter.writerow(line.values())