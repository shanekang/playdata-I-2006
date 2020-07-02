if(rescode ==200):
    response_json = json.load(response)
    jsondata.append(response_json)
#json_file=open('navernews/test.json', 'w', encoding='utf-8')
#json.dump(response_json, json_file, indent="\t", ensure_ascii=False)
    with open('navernews/test.json', 'w', encoding='utf-8') as make_file:
        json.dump(reponse_json, make_file, indent="\t",
                ensure_ascii=False)
else:
    print("Error code:" + rescode)    