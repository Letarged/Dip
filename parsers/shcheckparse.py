
import json

class shheaders:
    def __init__(self, address, result):
        self.address = address
        self.presentDict = result["present"] # detailed info 
        self.presentList = [] # just names of present headers
        for present_header in result["present"]:
            self.presentList.append(present_header)
        self.missing = result["missing"]
        self.numOfPresent = len(self.presentList)
        self.numOfMissing = len(self.missing)

# returns array of shheaders-class objects
# each reachable target is represented by 1 element in the array
def parse_output(output):
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")
    jsonStr = json.loads(data)
    shchecked_targets = []
    for addr in jsonStr:
        next_reccord = shheaders(addr, jsonStr[addr])
        shchecked_targets.append(next_reccord)
    
    return shchecked_targets


    
    print(shchecked_targets[0].address)
    print()
    print(shchecked_targets[0].presentList)
    print()
    print(shchecked_targets[0].presentDict)
    print()
    print(shchecked_targets[0].missing[2])
    print()
    print(shchecked_targets[0].numOfPresent)
    print(shchecked_targets[0].numOfMissing)

