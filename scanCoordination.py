import funcs
import configparser

settings = configparser.RawConfigParser()
settings.read('secondary/conf/settings.cfg') 



def performScanType1(targetS):

    config = configparser.RawConfigParser()
    config.read(settings['Path']['typeoneConf']) 
    ports_to_scan = config['Ports']['portslist']

    # if "--top-ports 10" is specified, leave it like that
    # but if "21,22,80,443,8080" is specified, we need to add "-p" prefix for nmap
    ports_to_command = ports_to_scan \
                        if ports_to_scan[:11] == "--top-ports" \
                        else "-p" + ports_to_scan
    nmap_command = settings['NmapOutput']['output'] + " " + ports_to_command

    temporary_dict = {}
    for target in targetS:
        temporary_dict[target] = funcs.nmapOpenPortsDiscoverScan(target, nmap_command)
        print("Went for " + str(target) + str(temporary_dict[target]))



    print() 
    for target in list(temporary_dict.keys()):
        for interestingport in temporary_dict[target].not_closed_not_filtered_ports():
            print(str(target) + " - " + str(interestingport))


def performScanType2(targetS):
    pass 