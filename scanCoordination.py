import funcs
import configparser
import secondary.scanCoordinationAssistant as assist

settings = configparser.RawConfigParser()
settings.read('secondary/conf/settings.cfg') 


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
        for interestingport in temporary_dict[target].not_closed_not_filtered_ports():
            match interestingport.port_service:
                case "https":
                        if config['Gobuster'].getboolean('switched_on'):
                            gobuster_command = assist.craftGobusterCommand(temporary_dict[target], interestingport, config)
                            gobuster_result = funcs.gobusterScan2(gobuster_command)
                            # print(gobuster_result)
                            print("Gobuster : " + str(gobuster_result)[:20])
                        if config['Whatweb'].getboolean('switched_on'):
                            whatweb_command = assist.craftWhatwebCommand(temporary_dict[target], interestingport, config, settings['WhatwebOutput']['output'])
                            whatweb_result=funcs.whatwebScan2(whatweb_command)
                            # print(whatweb_result)
                            print("Whatweb : " + str(whatweb_result)[:20])
                        if config['Nmapssl'].getboolean('switched_on'):
                            nmapssl_command = assist.craftNmapSSLCommand(temporary_dict[target], interestingport, config, settings['NmapOutput']['output'])
                            nmapssl_result = funcs.nmapSSLScan2(nmapssl_command) 
                            # print(nmapssl_result)
                            print("Nmapssl : " + str(nmapssl_result)[:20])
                        if config['Cewl'].getboolean('switched_on'):
                            cewl_command = assist.craftCewlCommand(temporary_dict[target], interestingport, config)
                            cewl_result = funcs.cewlScan2(cewl_command)
                            # print(cewl_result)
                            print("Cewl : " + str(cewl_result)[:20])
                case "domain":
                        if config['Dnsrecon'].getboolean('switched_on'):
                            dnsrecon_command = assist.craftDnsreconCommand(temporary_dict[target], interestingport, config, settings['DnsreconOutput']['output'])
                            print(dnsrecon_command)
                            dnsrecon_result = funcs.dnsreconScan2(dnsrecon_command)
                            # print(gobuster_result)
                            print("Dnsrecon : " + str(dnsrecon_result)[:20])
                        


def performScanType2(targetS):
    pass 