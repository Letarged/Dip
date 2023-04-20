import json 



def parse_output(output):
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")

   

    """
        This Json is an array of results, so each record is an element in the array.
        In order to access to the results, we need to specify [index].
    
    """
    jsonStr = json.loads(data)
   # print(jsonStr[0]["target"])
   # print(jsonStr[1]["target"])
    
    return jsonStr
