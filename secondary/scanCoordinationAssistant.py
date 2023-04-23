import ipaddress
from urllib.parse import urlparse
import socket
import classes


def check_ip_or_url(value):
    parsed = urlparse(value)
    if parsed.scheme:
        return "url"
    else:
        try:
            ip = ipaddress.ip_address(value)
            return "ip"
        except ValueError:
            exit("Err")

"""
         https:// 
            +
        target.com
            + 
          :443
""" 
def getFullUrl(target, port, with_port_suffix):
    if with_port_suffix:
        if port.port_service == "http":
            target = "http://" + str(target.address) + ":" + str(port.num)
        elif port.port_service == "https":
            target = "https://" + str(target.address) + ":" + str(port.num)
    else:
        if port.port_service == "http":
            target = "http://" + str(target.address)
        elif port.port_service == "https":
            target = "https://" + str(target.address)
    
    return target



def craftGobusterCommand(target, port, config):
   # gobuster_target = getFullUrl(target, port,1)

    if check_ip_or_url(target.address) == "ip":
        tmp_trgt = socket.gethostbyaddr(target.address)[0]
        
        x = classes.ip(tmp_trgt, port)
        gobuster_target = getFullUrl(x, port, 1)
    elif check_ip_or_url(target.address) == "url":
        gobuster_target = getFullUrl(target, port, 1)

    command = (
               # "dir " + 
                config['Gobuster']['params'] + 
                " " + 
                config['Gobuster']['excludeErrCodes'] + 
                " " + 
                " -w " + config['Gobuster']['wordlist'] + 
                " -u " + gobuster_target
    )

    print(command)
    return command
   
def craftWhatwebCommand(target, port, config, output_format):
    whatweb_target = getFullUrl(target, port,1)
    command = (
        output_format + 
        " " + 
        config['Whatweb']['params'] + 
        " " + 
        config['Whatweb']['aggression'] + 
        " " + 
       # "-p" + str(port.num) + 
        " " +
        whatweb_target

    )
    return command

def craftNmapSSLCommand(target, port, config, output_format): 
    command = (
        output_format + 
        " " + 
        config['Nmapssl']['params'] + 
        " " + 
        "-p " + str(port.num) +
        " " +
        str(target.address)

    )   
    return command

def craftCewlCommand(target, port, config):
    cewl_target = getFullUrl(target,port,1)
    command = (
        config['Cewl']['params'] + 
        " " +
        cewl_target

    )   
    return command

def craftDnsreconCommand(target, port, config, output_format):

    if check_ip_or_url(target.address) == "ip":
        dns_target = socket.gethostbyaddr(target.address)[0]
    elif check_ip_or_url(target.address) == "url":
        dns_target = target.address

    command = (
        output_format + 
        " " + 
        config['Dnsrecon']['type'] + 
        " " + 
        config['Dnsrecon']['params'] + 
        " " + 
        " -d " +
        str(dns_target)
    )
    return command

def craftShcheckCommand(target, port, config, output_format):
    shcheck_target = getFullUrl(target,port,0)
    command = (
        output_format + 
        " " + 
        config['Dnsrecon']['params'] + 
        " -p" + str(port.num) + 
        " " +
        shcheck_target
    )
    return command



def craftHostDiscoveryNmapCommand(target, config, output_format):
    command = (
            output_format + 
            " " + 
            config['TypeOfScan']['type'] + 
            " " + 
            target

        )   
    print(command)
    return command, config['TypeOfScan']['type']