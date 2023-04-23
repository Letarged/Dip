import json
import xmltodict

import classes # user-defined module

def nmap_output_proccess(jsonStr, debug_on):
    tmp = []
    
    # if all the scanned ports are closed
    if "port" not in jsonStr["nmaprun"]["host"]["ports"]:
      return []

    # in case of exactly 1 open port (we need it to be an array of 1 element, not just that 1 element)
    if isinstance(jsonStr["nmaprun"]["host"]["ports"]["port"], dict):
      jsonStr["nmaprun"]["host"]["ports"]["port"] = [jsonStr["nmaprun"]["host"]["ports"]["port"]]

    for i in jsonStr["nmaprun"]["host"]["ports"]["port"]:
        # if there is no service, it should mean the port is closed
        if not "service" in i:
          continue
 
        one_port = classes.port(int(i["@portid"]),i["state"]["@state"],i["service"]["@name"] )
        tmp.append(one_port)

    return tmp

# bude sa musieť upraviť, lebo nie všetky nástroje majú xmlko ako nmap
# update -> už som to osamostatnil, len ešte stále to je ako keby pripravené robiť switch, to už teda netreba
def parse_output(target, output, debug_on):
   # for line in output.logs(stream=True):
        #if debug_on: print(line)
  #  if debug_on: print("#############") 
  #  if debug_on: print("#############") 
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")
   # if debug_on: print(data)
   # if debug_on: print("#############")
   # if debug_on: print("#############")
    data = json.dumps(xmltodict.parse(data), indent=4)
    jsonStr = json.loads(data)

    tmp = nmap_output_proccess(jsonStr, debug_on)
    return classes.ip(target, tmp)
    