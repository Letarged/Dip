import json 



def parse_output(output):
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")
    jsonStr = json.loads(data)
    print(jsonStr[1]["target"])
    
    return jsonStr
