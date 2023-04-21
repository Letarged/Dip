import funcs
import netifaces
import ipaddress
import configparser
import secondary.scanCoordinationAssistant as assist

settings = configparser.RawConfigParser()
settings.read('secondary/conf/settings.cfg') 



def netmaskToSlash(netmask):
        ip_network = ipaddress.IPv4Network("0.0.0.0/" + netmask, strict=False)
        return ip_network.prefixlen

def getInterfaces(configInterfaces, logic):
    lst = []
    if logic == True:
        for interf in configInterfaces:
            if configInterfaces.getboolean(interf) == False:
                lst.append(interf)
    else:
        for interf in configInterfaces:
            if configInterfaces.getboolean(interf) == True:
                lst.append(interf)
    return lst

"""
    [Logic]
    1 = if an interface is not explicitly forbidden, then it's allowed (even if not listed above)
      = so "lst" is composed of the forbidden interfaces
    0 = allow only those interfaces, which are listed and has "True / 1" value
      = so "lst" is composed of the allowed interfaces

"""
def gonna_be_scanned(lst, interface, logic):
    if logic == True:
        if len(interface) == 2:
            if interface in lst:
                return False
        else:
            if (interface in lst) or (interface[:(len(interface)-1)] in lst):
                return False
        return True
    else:
        if len(interface) == 2:
            if interface in lst:
                return True
        else:
            if (interface in lst) or (interface[:(len(interface)-1)] in lst):
                return True
        return False
    

        
    

            

# This is the main function for coordinating type-1-scan
# It should perform all the steps specified in the confing file, 
#       one after antoher, adjusting the steps according 
#       to the results from initial nmap ports discovery
def performScanType1(targetS, debug_on):

    config = configparser.RawConfigParser()
    config.read(settings['Path']['typeoneConf']) 
    ports_to_scan = config['Ports']['portslist']

    # if "--top-ports 10" is specified, leave it like that
    # but if "21,22,80,443,8080" is specified, we need to add "-p" prefix for nmap
    ports_to_command = ports_to_scan \
                        if ports_to_scan[:11] == "--top-ports" \
                        else "-p" + ports_to_scan
    nmap_command = settings['NmapOutput']['output'] + " " + config['Typeofnmapscan']['nmaptype'] +  " " + ports_to_command

    temporary_dict = {}
    for target in targetS:
        temporary_dict[target] = funcs.nmapOpenPortsDiscoverScan(target, nmap_command, debug_on)
        if debug_on: print("Went for " + str(target) + str(temporary_dict[target]))



    if debug_on:
        for target in list(temporary_dict.keys()):
            for interestingport in temporary_dict[target].not_closed_not_filtered_ports():
                print(str(target) + " - " + str(interestingport.num) + " " + str(interestingport.port_service))
                print(type(interestingport))


          
    for target in list(temporary_dict.keys()):
        print("-----------------------")
        for interestingport in temporary_dict[target].not_closed_not_filtered_ports():
            match interestingport.port_service:
                case "https":
                        if config['Gobuster'].getboolean('switched_on'):
                            gobuster_command = assist.craftGobusterCommand(temporary_dict[target], interestingport, config)
                            gobuster_result = funcs.gobusterScan2(gobuster_command)
                            # print(gobuster_result)
                            print("Gobuster : " + str(gobuster_result)[:50])
                        if config['Whatweb'].getboolean('switched_on'):
                            whatweb_command = assist.craftWhatwebCommand(temporary_dict[target], interestingport, config, settings['WhatwebOutput']['output'])
                            whatweb_result=funcs.whatwebScan2(whatweb_command)
                            # print(whatweb_result)
                            print("Whatweb : " + str(whatweb_result)[:50])
                        if config['Nmapssl'].getboolean('switched_on'):
                            nmapssl_command = assist.craftNmapSSLCommand(temporary_dict[target], interestingport, config, settings['NmapOutput']['output'])
                            nmapssl_result = funcs.nmapSSLScan2(nmapssl_command) 
                            # print(nmapssl_result)
                            print("Nmapssl : " + str(nmapssl_result)[:50])
                        if config['Cewl'].getboolean('switched_on'):
                            cewl_command = assist.craftCewlCommand(temporary_dict[target], interestingport, config)
                            cewl_result = funcs.cewlScan2(cewl_command)
                            # print(cewl_result)
                            print("Cewl : " + str(cewl_result)[:20])
                        if config['Shcheck'].getboolean('switched_on'):
                            shcheck_command = assist.craftShcheckCommand(temporary_dict[target], interestingport, config, settings['ShcheckOutput']['output'])
                            shcheck_result = funcs.shcheckScan2(shcheck_command)
                            # print(cewl_result)
                            print("Shcheck : " + str(shcheck_result))
                case "domain":
                        if config['Dnsrecon'].getboolean('switched_on'):
                            dnsrecon_command = assist.craftDnsreconCommand(temporary_dict[target], interestingport, config, settings['DnsreconOutput']['output'])
                            print(dnsrecon_command)
                            dnsrecon_result = funcs.dnsreconScan2(dnsrecon_command)
                            # print(gobuster_result)
                            print("Dnsrecon : " + str(dnsrecon_result)[:50])
                        
def performScanType0(scan_after_discovery, debug_on):
    
    config = configparser.RawConfigParser()
    config.read(settings['Path']['typezeroConf']) 

    our_interfaces = getInterfaces(config['Interfaces'], config['Logic'].getboolean('negative'))
    interfaces = netifaces.interfaces()

    potentional_targets = []
    for inter in interfaces:
        if gonna_be_scanned(our_interfaces, inter, config['Logic'].getboolean('negative')):
            ip = netifaces.ifaddresses(inter)[netifaces.AF_INET][0]['addr']
            netmask = netifaces.ifaddresses(inter)[netifaces.AF_INET][0]['netmask']
            full_ip = str(ip) + "/" + str(netmaskToSlash(netmask))
           # potentional_targets.append(str(inter) + " : " + str(full_ip))
            potentional_targets.append(str(full_ip))
    print(potentional_targets)

    for target in potentional_targets:
        discovery_command, parameter = assist.craftHostDiscoveryNmapCommand(target, config,settings['NmapOutput']['output'])
        discovery_result = funcs.nmapDiscoverScan(discovery_command, parameter)
        print(discovery_result)
        print(scan_after_discovery)
        print(type(scan_after_discovery))
        
    match scan_after_discovery:
        case '0':
            pass
        case '1':
            performScanType1(discovery_result, debug_on)
        case '2':
            performScanType2(discovery_command, debug_on)


def performScanType2(targetS, debug_on):
    pass 