import ipaddress
from urllib.parse import urlparse
import socket
import classes


def check_ip_or_url(value):
    try:
        ip = ipaddress.ip_address(value)
        return "ip"
    except:
        return "url"


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
        " -w " + config['Gobuster']['wordlist'] +
        " -u " + gobuster_target
    )

    print(command)
    return command, config['Gobuster']['params']


def craftWhatwebCommand(target, port, config, output_format):
    whatweb_target = getFullUrl(target, port, 1)
    command = (
        output_format +
        " " +
        config['Whatweb']['params'] +
        " " +
        #     config['Whatweb']['aggression'] +
        " " +
        # "-p" + str(port.num) +
        " " +
        whatweb_target

    )
    return command, config['Whatweb']['params']


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

    return command, config['Nmapssl']['params']


def craftCewlCommand(target, port, config):
    cewl_target = getFullUrl(target, port, 1)
    command = (
        config['Cewl']['params'] +
        " " +
        cewl_target

    )
    return command, config['Cewl']['params']


def craftDnsreconCommand(target, config, output_format):

    if check_ip_or_url(target.address) == "ip":
        dns_target = socket.gethostbyaddr(target.address)[0]
    elif check_ip_or_url(target.address) == "url":
        dns_target = target.address

    command = (
        output_format +
        " " +
        config['Dnsrecon']['params'] +
        " " +
        " -d " +
        str(dns_target)
    )
    return command, config['Dnsrecon']['params']


def craftShcheckCommand(target, port, config, output_format):
    
    shcheck_target = getFullUrl(target, port, 0)
    command = (
        output_format +
        " " +
        config['Shcheck']['params'] +
        " -p" + str(port.num) +
        " " +
        shcheck_target
    )
   
    return command, config['Shcheck']['params']


def craftHostDiscoveryNmapCommand(target, config, output_format):

    command = (
        output_format +
        " " +
        config['TypeOfScan']['params'] +
        " " +
        target

    )
    print(command)
    return command, config['TypeOfScan']['params']


def craftNmapCommand(target, config, output_format):
    ports_to_scan = config['Nmap']['ports']

    # if "--top-ports 10" is specified, leave it like that
    # but if "21,22,80,443,8080" is specified, we need to add "-p" prefix for nmap
    ports_to_command = ports_to_scan \
        if ports_to_scan[:11] == "--top-ports" \
        else "-p" + ports_to_scan
    nmap_command = (
        output_format +
        " " +
        config['Nmap']['params'] +
        " " +
        ports_to_command +
        " " +
        target


    )

    return nmap_command, config['Nmap']['params']


def craftMasscanCommand(target, config, output_format):
    if check_ip_or_url(target) == "url":
        target = socket.gethostbyname(target)

    ports_to_scan = config['Masscan']['ports']

    # if "--top-ports 10" is specified, leave it like that
    # but if "21,22,80,443,8080" is specified, we need to add "-p" prefix for nmap
    ports_to_command = ports_to_scan \
        if ports_to_scan[:11] == "--top-ports" \
        else "-p" + ports_to_scan

    masscan_command = (
        output_format +
        " " +
        config['Masscan']['params'] +
        " " +
        ports_to_command +
        " " +
        target
    )
    print(masscan_command)
    return masscan_command, config['Masscan']['params']
