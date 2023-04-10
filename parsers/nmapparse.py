import json
import xmltodict

import classes # user-defined module

def nmap_output_proccess(jsonStr):
    tmp = []

    for i in jsonStr["nmaprun"]["host"]["ports"]["port"]:
    # tmp.append({i["@portid"] : i})
        one_port = classes.port(int(i["@portid"]),i["state"]["@state"],i["service"]["@name"] )
        tmp.append(one_port)

    return tmp

# bude sa musieť upraviť, lebo nie všetky nástroje majú xmlko ako nmap
# update -> už som to osamostatnil, len ešte stále to je ako keby pripravené robiť switch, to už teda netreba
def parse_output(target, output):
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")

    data = json.dumps(xmltodict.parse(data), indent=4)
    jsonStr = json.loads(data)

    tmp = nmap_output_proccess(jsonStr)
    return classes.ip(target, tmp)
    