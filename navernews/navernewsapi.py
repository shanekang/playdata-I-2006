import csv
import json

input_file_name = "navernews/travel.csv"
output_file_name = "navernews/traveltest.json"

input_file = open(input_file_name, "r", encoding="utf-8", newline="")
output_file = open(output_file_name, "w", encoding="utf-8", newline="")

reader = csv.reader(input_file)
col_names = next(reader)

for cols in reader:
    doc = {
        col_name: col for col_name, col in zip(col_names, cols)}#zip은 튜플형태로 묶어준다
     
    print(json.dumps(doc, ensure_ascii=False), file=output_file)