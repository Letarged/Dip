import docker # for docker images and containers managment
import configparser # for parsing the configuration file
from ftplib import FTP

from secondary.dockerimages import images

import parsers.nmapparse as nmapparse
import parsers.shcheckparse as shcheckparse
import parsers.cewlparse as cewlparse
import parsers.whatwebparse as whatwebparse
import parsers.masscanparse as masscanparse
import parsers.dnsreconparse as dnsreconparse
import parsers.gobusterparse as gobusterparse
import parsers.nmapSSLparse as nmapSSLparse


config = configparser.RawConfigParser()
config.read('secondary/conf/p.cfg')



def nmapOpenPortsDiscoverScan(target, nmap_command, debug_on):
    dckr = docker.from_env()
    x = dckr.containers.run(images["nmap"], " " + nmap_command + " " + target, detach = True)
    output = dckr.containers.get(x.id)
    
    return nmapparse.parse_output(
        target, output, debug_on
    )

def nmapDiscoverScan(target):

    #XXX

    try:
        config["Nmap"]["possibleports"]
        possibleports = True
    except:
        possibleports = False

    

    #XXX

    dckr = docker.from_env()
    x = dckr.containers.run(images["nmap"], config['Nmap']['params'] + " " + target, detach = True)


  #  f = open(nmap_file_out, "r+")
  #  data = ""
    output = dckr.containers.get(x.id)
    
    return nmapparse.parse_output(
        target, output
    )


def cewlScan(target_ip, port):
    dckr = docker.from_env()
    print("In cewl: " + str(target_ip.address) + " " + str(port.num) + " " + port.state + " " + port.port_service)
    service = port.port_service
    if service == "http":
        cewl_target = "http://" + str(target_ip.address)
    elif service == "https":
        cewl_target = "https://" + str(target_ip.address )
        print(cewl_target)
    x = dckr.containers.run(images["cewl"], config['Cewl']['params'] + " " + cewl_target, detach = True) 
    output = dckr.containers.get(x.id)
    return cewlparse.parse_output(
        output
    )


def shcheckScan(target_ip, port):
    dckr = docker.from_env()
    print("I am SH-check!" + str(port))
    service = port.port_service
    if service == "http":
        shcheck_target = "http://" + str(target_ip.address)
    elif service == "https":
        shcheck_target = "https://" + str(target_ip.address )
    else:
        raise("Err # TODO")
    print(shcheck_target)
    print(images["shcheck"])
    x = dckr.containers.run(images["shcheck"], config['Shcheck']['params'] + " " + shcheck_target, detach = True) 
    output = dckr.containers.get(x.id)
    
    return shcheckparse.parse_output(
        output
    )


def whatwebScan(target):
    dckr = docker.from_env()
    x = dckr.containers.run(images["whatweb"], config['Whatweb']['params'] + " " + target.address, detach = True )
    output = dckr.containers.get(x.id)
    
    return whatwebparse.parse_output(
        output
    )


# Masscan potrebuje porty, v configuraku je zatial top 10
def masscanScan(target):
    dckr = docker.from_env()
    x = dckr.containers.run(images["masscan"], config['Masscan']['params'] + " " + target.address, detach = True )

    output = dckr.containers.get(x.id)

    return masscanparse.parse_output(
        output
    )

def dnsreconScan(target):
    dckr = docker.from_env()
    x = dckr.containers.run(images["dnsrecon"], config['Dnsrecon']['params'] + " " + target.address, detach = True )
   # with open(dnsjsonfile, 'r') as file:
     #   output = file.read()
    
    output = dckr.containers.get(x.id)
   

    return dnsreconparse.parse_output(
        output
    )


def nmapSSLScan(target_ip):
    dckr = docker.from_env()
    x = dckr.containers.run(images["nmap"],
                            config["Nmap"]["sslcert"] + " " +
                            target_ip.address,
                            detach=True
                            )
    output = dckr.containers.get(x.id)
    
    return nmapSSLparse.parse_output(
        output)

def gobusterScan(target_ip, port):

    dckr = docker.from_env()

    
    if port.port_service == "http":
        gobuster_target = "http://" + str(target_ip.address)
    elif port.port_service == "https":
        gobuster_target = "https://" + str(target_ip.address)
    x = dckr.containers.run(images["gobuster"], 
                            config['Gobuster']['params'] + 
                            " " + " -w " + config['Gobuster']['wordlist'] +
                            " " + " -u " + gobuster_target,
                            detach = True )
    


    output = dckr.containers.get(x.id)
   

    return gobusterparse.parse_output(
        output
    )


def checkForFtpAnon(target_ip):
    ftp = FTP(target_ip.address)
    resp = ftp.login()
    print(resp)
    exit()