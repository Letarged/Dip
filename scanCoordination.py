import funcs
import configparser

settings = configparser.RawConfigParser()
settings.read('secondary/conf/settings.cfg') 


def performScanType1(targetS):

    config = configparser.RawConfigParser()
    config.read(settings['Path']['typeoneConf']) 
    print(config['Ports']['portslist'])
    exit()

    temporary_dict = {}
    for target in targetS:
        temporary_dict[target] = funcs.nmapDiscoverScan(target)

    print() 
    print("........")
    for target in list(temporary_dict.keys()):
        for interestingport in temporary_dict[target].not_closed_not_filtered_ports():
            print(str(target) + " - " + str(interestingport))
  #  print(temporary_dict[list(temporary_dict.keys())[0]].not_closed_not_filtered_ports()[0].num)     
    exit()


def performScanType2(targetS):
    pass 