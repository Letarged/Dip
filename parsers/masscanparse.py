import json

def parse_output(output):
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")
   
    data = data.split("\n",3)[3].strip() # remove the annoying masscan header lines
    data = data[:data.rfind("\nrate")] # remove last line
    print("-------")
    print(data)
    print("-------")

    jsonStr = json.loads(data)
    print(jsonStr[1]["ports"])
    return jsonStr
    