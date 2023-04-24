import json
import xmltodict

import classes # user-defined module

"""
  Returns list of IP targets.
    (this function is for "-sn" parameter of nmap)
"""
def nmap_output_proccess_sn(jsonStr):
  tmp = []
  for i in jsonStr["nmaprun"]["host"]:
      tmp.append(i["address"]["@addr"])

  return tmp
  


def parse_output(output):
  data = ""
  
  for line in output.logs(stream=True):
      data += line.decode("utf-8")

  data = json.dumps(xmltodict.parse(data), indent=4)
  jsonStr = json.loads(data)
  return nmap_output_proccess_sn(jsonStr)
    