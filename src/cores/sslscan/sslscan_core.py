from secondary.dockerimages import modules
from dckrChiefExecutive import launchTheScan
from cores.helper import getFullUrl_from_URI
from termcolor import colored

def craftSSLSCANCommand(target, port, params):
    cewl_target = getFullUrl_from_URI(target, port, 1)
    command = (
        params + 
        " " + 
        target #+ 
       # " -w " +
        #outputfile
    )
    print(command)
    return command



def run(target,port, modulename, params):
    command = craftSSLSCANCommand(target, port, params)
    result = launchTheScan(
        modules[modulename], 
        command, 
        )

    print(result)