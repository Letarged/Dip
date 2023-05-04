#!/usr/bin/python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Good page for NMAP 
# https://securitytrails.com/blog/nmap-commands 

import docker # for docker images and containers managment
import sys # for sys.argv
import json
import classes # user module "classes.py"
import funcs # functions
from secondary.dockerimages import images 
import argParser 
import scanCoordination
import time 


debug_on = False
start_time = time.time()

def main():
    scanType, targetS = argParser.process_cmd_arguments(debug_on)


    """

    Different meaning of "scanType" variable:

        targetS == []  ->   scanType determins what's happening AFTER potentional targets are discovered
        targetS != []  ->   scanType determins wheter we are running scan1 or scan2 on the given targets

    """

    if targetS == []:
        scanCoordination.performScanType0(scanType, debug_on)
    else:
        match scanType:
            case '1':
                scanCoordination.performScanType1(targetS, debug_on)
            case '2':
                scanCoordination.performScanType2(targetS, debug_on)
            case _:
                print("Incorrect place in the multiverse.")

    end_time = time.time()
    print("\nDone in " + str("{:.4f}".format(end_time - start_time)) + " seconds.")

    exit()

if __name__ == '__main__':
    main()

"""
for x in target_addr.not_closed_not_filtered_ports():
    match x.num:


        case 21:
            funcs.checkForFtpAnon(target_addr)


        case 443:
            print("It's 443")
            sh_result = funcs.shcheckScan(target_addr, x) 
            print("Missing: " + str(sh_result[0].missing))
            cewl_result = funcs.cewlScan(target_addr, x) # TODO možno zbytočne dávať port ako argument? To isté aj v ostatných prípadoch?
            print("Cewl first 10: " + str(cewl_result[:10]))
        
           # whatweb_result = funcs.whatwebScan(target_addr)
           # masscan_result = funcs.masscanScan(target_addr)
            #print(masscan_result)
          #  dnsrecon_result = funcs.dnsreconScan(target_addr)
           # print(whatweb_result)

          #  gobuster_result = funcs.gobusterScan(target_addr, x) # TODO možno zbytočne dávať port ako argument? To isté aj v ostatných prípadoch?
            ssl_results = funcs.nmapSSLScan(target_addr)
            #print(ssl_results)
            print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in ssl_results.items()) + "}")


        case 80:
            print("It's 80")
        case _:
            print("Default action... :D " + str(x))




 Toto asi nič 

for x in target_list.ports:
    if x.state == "open":
        funcs.deeperScan(target_list, x)
"""