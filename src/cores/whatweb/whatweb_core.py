from secondary.dockerimages import modules
from cores.helper import getFullUrl_from_URI
from dckrChiefExecutive import launchTheScan


def craftWhatwebCommand(target, port, params, output_format):
    whatweb_target = getFullUrl_from_URI(target, port, 1)
    command = (
        output_format +
        " " +
        params +
        " " +
        whatweb_target
    )
    return command

def run(target, port, modulename,params ):
    output_format = '--log-json=- -q'
    whatweb_cmd = craftWhatwebCommand(target, port, params, output_format)
    whatweb_result = launchTheScan(
        modules[modulename],
        whatweb_cmd
    )
    print(whatweb_result)
    return
    