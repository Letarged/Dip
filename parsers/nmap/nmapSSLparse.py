import json
import xmltodict

def process_ssl_json(jsonSSL):
    tmp = {}
    tmp["ip"] = jsonSSL["nmaprun"]["host"]["address"]["@addr"]
    tmp["iptype"] = jsonSSL["nmaprun"]["host"]["address"]["@addrtype"]
    tmp["hostname"] = jsonSSL["nmaprun"]["host"]["hostnames"]["hostname"]
    tmp["service"] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["service"]
    #tmp["XXX"] =  jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][1]["elem"][0]["@key"]
    #tmp[jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][1]["elem"][0]["@key"]] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][1]["elem"][0]["#text"]
    
    size_of_arr = len(jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][1]["elem"])
    for i in range(size_of_arr):
        tmp[jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][1]["elem"][i]["@key"]] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][1]["elem"][i]["#text"]
    
    size_of_arr = len(jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][2]["elem"])
    for i in range(size_of_arr):
        tmp[jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][2]["elem"][i]["@key"]] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][2]["elem"][i]["#text"]

    size_of_outer_arr = len(jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][3]["table"])
    for x in range(size_of_outer_arr):
        size_of_inner_arr = len(jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][3]["table"][x]["elem"])
        for y in range(size_of_inner_arr):
            tmp[jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][3]["table"][x]["elem"][y]["@key"]] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][3]["table"][x]["elem"][y]["#text"]

    # valid from:
    tmp[jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][4]["elem"][0]["@key"]] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][4]["elem"][0]["#text"]
    # valid until:
    tmp[jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][4]["elem"][1]["@key"]] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["table"][4]["elem"][1]["#text"]

    size_of_arr = len(jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["elem"])
    
    for i in range(size_of_arr):
        tmp[jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["elem"][i]["@key"]] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["elem"][i]["#text"]

    tmp["type_of_cert"] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["@id"]
    tmp["tldr"] = jsonSSL["nmaprun"]["host"]["ports"]["port"]["script"]["@output"]


    return tmp
def parse_output(output):
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")


    data = json.dumps(xmltodict.parse(data), indent=4)
    jsonStr = json.loads(data)

    return process_ssl_json(jsonStr)

    
    