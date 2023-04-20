import json

def parse_output(output):
    data = ""
    for line in output.logs(stream=True):
        data += line.decode("utf-8")
    data = data.split("[*]", 1)[0]

    print(data) # XXX
    exit() # XXX

    jsonStr = json.loads(data)
    return jsonStr

    # finish testing and organizing json output
