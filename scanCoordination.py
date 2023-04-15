import funcs
import configparser

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




    for target in list(temporary_dict.keys()):
        for interestingport in temporary_dict[target].not_closed_not_filtered_ports():
            if debug_on: print(str(target) + " - " + str(interestingport))


def performScanType2(targetS):
    pass 