import funcs
import netifaces
import ipaddress
import configparser
import secondary.scanCoordinationAssistant as assist
import time
import threading

settings = configparser.RawConfigParser()
settings.read('secondary/conf/settings.cfg') 

def display_loading():
    counter = 0
    while True:
        if counter % 6 == 0:
            print("\rGobuster in progress ", end="")
        print(".", end="", flush=True)
        time.sleep(0.9)
        counter += 1
        if counter >= 30:
            break


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
    

        
    
def portScanningPhase(targetS, config):
    doneAtLeastOneScan = False
    nmap_found_targets = {} 
    masscan_found_target = {}
    if config['Nmap'].getboolean('switched_on'):
        doneAtLeastOneScan = True
        for target in targetS:
            nmap_command, param = assist.craftNmapCommand(target, config, settings['NmapOutput']['output'])
            nmap_found_targets[target] = funcs.launchTheScan("nmap", nmap_command, param)
            #if debug_on: print("Went for " + str(target) + str(found_targets[target]))

    if config['Masscan'].getboolean('switched_on'):
        doneAtLeastOneScan = True
        for target in targetS:
            masscan_command, param = assist.craftMasscanCommand(target, config, settings['MasscanOutput']['output'])
            masscan_found_target[target] = funcs.launchTheScan("masscan", masscan_command, param)
    
    if not doneAtLeastOneScan:
        exit("At least one scan must be performed:  nmap / masscan")

    to_s_cim_pracujeme = {**masscan_found_target, **nmap_found_targets}

    for x in list(to_s_cim_pracujeme.keys()):
        print("LULU: " + str(x))
        for port in to_s_cim_pracujeme[x].not_closed_not_filtered_ports():
            print(port)

    #print(str(type(masscan_found_target)))
    #print(nmap_found_targets[next(iter(nmap_found_targets))])
   # print(nmap_found_targets['whiskeyprovsechny.cz'])
   # return(masscan_found_target.update(nmap_found_targets))
    return {**nmap_found_targets, **masscan_found_target}
    #exit()
    # print("THIS: " + str(masscan_found_target.update(nmap_found_targets))) # TODO NAPIČU LEBO NASTANE OVERWRITE (takto to je zatiaľ len ako proforma)

# This is the main function for coordinating type-1-scan
# It should perform all the steps specified in the confing file, 
#       one after antoher, adjusting the steps according 
#       to the results from initial nmap ports discovery
def performScanType1(targetS, debug_on):

    config = configparser.RawConfigParser()
    config.read(settings['Path']['typeoneConf']) 
    
    found_targets = portScanningPhase(targetS, config)

    """
    for target in list(fKazanjian vestibuloplasty and Edlan Mejchar vestibuloplasty are two different surgical techniques used to increase the depth of the oral vestibule, which is the space between the teeth and the cheeks or lips.

Kazanjian vestibuloplasty involves making an incision in the mucosa of the oral vestibule and then deepening the vestibule by creating a space between the mucosa and the underlying bone. This space is then filled with a graft material, such as autogenous or alloplastic materials, to provide support for the mucosa and maintain the increased vestibular depth.

On the other hand, Edlan Mejchar vestibuloplasty involves making incisions at the junction of the attached gingiva and the mucosa of the oral vestibule. These incisions are then extended laterally and vertically to create a flap of mucosa and attached gingiva that is then elevated and repositioned coronally to increase the depth of the vestibule.

Both techniques aim to increase the depth of the vestibule, but they differ in their approach and surgical technique. The choice of technique depends on the individual patient's needs and the surgeon's experience and preference.ound_targets.keys()):
        print("HERE: " + str(target) + "  :: " + str(found_targets[target]))
        for interestingport in found_targets[target].not_closed_not_filtered_ports():
            print(str(target) + " - " + str(interestingport.num) + " " + str(interestingport.port_service))
    """

          
    for target in list(found_targets.keys()):
        print("-----------------------")
        for interestingport in found_targets[target].not_closed_not_filtered_ports():
            match interestingport.port_service:
                case "https":
                        if config['Gobuster'].getboolean('switched_on'):
                            gobuster_command, params = assist.craftGobusterCommand(found_targets[target], interestingport, config)
                            loading_thread = threading.Thread(target=display_loading)
                            loading_thread.start()
                            gobuster_result = funcs.launchTheScan("gobuster", gobuster_command, params)
                            loading_thread.join()
                            # print(gobuster_result)
                            print("Gobuster : " + str(gobuster_result)[:50])

                        if config['Whatweb'].getboolean('switched_on'):
                            whatweb_command, params = assist.craftWhatwebCommand(found_targets[target], interestingport, config, settings['WhatwebOutput']['output'])
                            whatweb_result=funcs.launchTheScan("whatweb",whatweb_command, params)
                            # print(whatweb_result)
                            print("Whatweb : " + str(whatweb_result)[:50])

                        if config['Nmapssl'].getboolean('switched_on'):
                            nmapssl_command, params = assist.craftNmapSSLCommand(found_targets[target], interestingport, config, settings['NmapOutput']['output'])
                            nmapssl_result = funcs.launchTheScan("nmap", nmapssl_command, params) 
                            # print(nmapssl_result)
                            print("Nmapssl : " + str(nmapssl_result)[:50])

                        if config['Cewl'].getboolean('switched_on'):
                            cewl_command, params = assist.craftCewlCommand(found_targets[target], interestingport, config)
                            cewl_result = funcs.launchTheScan("cewl", cewl_command, params)
                            # print(cewl_result)
                            print("Cewl : " + str(cewl_result)[:20])

                        if config['Shcheck'].getboolean('switched_on'):
                            """ Following line ensures that shcheck will get https://site.org and not IP address, because in that case shcheck gives an error"""
                            found_targets[target].address = target
                            shcheck_command, params = assist.craftShcheckCommand(found_targets[target], interestingport, config, settings['ShcheckOutput']['output'])
                            shcheck_result = funcs.launchTheScan("shcheck", shcheck_command, params)
                            print(shcheck_result)
                case "domain":
                        if config['Dnsrecon'].getboolean('switched_on'):
                            dnsrecon_command, params = assist.craftDnsreconCommand(found_targets[target], config, settings['DnsreconOutput']['output'])
                            dnsrecon_result = funcs.launchTheScan("dnsrecon", dnsrecon_command, params)
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
        discovery_result = funcs.launchTheScan("nmap", discovery_command, parameter)
        print(discovery_result)

    match scan_after_discovery:
        case '0':
            pass
        case '1':
            performScanType1(discovery_result, debug_on)
        case '2':
            performScanType2(discovery_command, debug_on)


def performScanType2(targetS, debug_on):
    pass 