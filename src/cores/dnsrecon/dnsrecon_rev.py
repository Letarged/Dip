
from secondary.dockerimages import modules
from dckrChiefExecutive import launchTheScan
from cores.helper import check_ip_or_url, ip_to_range
import socket

def craftDnsReverseLookupCommand(target, params, output_format):

    if check_ip_or_url(target) == "ip":
        dns_target = target
    elif check_ip_or_url(target) == "url":
        dns_target = socket.gethostbyname(target)
        
   
    dns_target = ip_to_range(dns_target)


    command = (
        output_format +
        " " +
        params +
        " -r " +
        str(dns_target)
    )
    return command


def run(target,port, modulename, params):
    output_format = '--json=/dev/stdout'
    dnsrecon_command = craftDnsReverseLookupCommand(target, params, output_format)
    result = launchTheScan(
        modules[modulename], 
        dnsrecon_command, 
        )
    print(result)