import json
import xmltodict
from termcolor import colored

def extract_cipher_info(data):
    if 'document' not in data or 'ssltest' not in data['document']:
        return ""
    cipher_info = ""
    cipher_strength = {'anonymous': [], 'null': [], 'weak': [], 'acceptable': [], 'medium': [], 'strong': []}
    
    for cipher in data['document']['ssltest']['cipher']:
        if '@strength' in cipher and cipher['@strength'] in cipher_strength:
            cipher_strength[cipher['@strength']].append(cipher)
    for strength in ['anonymous', 'null', 'weak', 'acceptable', 'medium', 'strong']:
        if cipher_strength[strength]:
            cipher_info += colored(f"{strength.capitalize()} ciphers:\n", 'blue', attrs=['bold', 'dark'])
            sorted_ciphers = sorted(cipher_strength[strength], key=lambda x: int(x['@bits']), reverse=True)
            for cipher in sorted_ciphers:
                cipher_info += f"\t{colored(cipher['@sslversion'], 'red')} {colored(cipher['@bits'], 'green', attrs=['dark'])} {colored('bits', 'green', attrs=['dark'])} {colored(cipher['@cipher'], 'cyan')}\n"
    return cipher_info


def extract_enabled_protocols(json_str):
    result = [colored("Enabled protocols:", 'blue', attrs=["bold", "dark"])]
    protocols = json_str["document"]["ssltest"]["protocol"]
    enabled_protocols = [colored(f"              {p['@type']} {p['@version']}", 'blue') for p in protocols if p["@enabled"] == "1"]
    result.extend(enabled_protocols)
    return "\n".join(result) + '\n'

def parse_output(output):
 
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")
  
    data = json.dumps(xmltodict.parse(data), indent=4)
    jsonStr = json.loads(data)
    
    result =    extract_enabled_protocols(jsonStr) + \
                extract_cipher_info(jsonStr)
    return result
    