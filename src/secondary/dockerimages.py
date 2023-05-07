images = {
    'nmap' : 'dnmap:v1',
    'cewl' : 'dcewl:v1',
    'shcheck' : 'dshcheck:v1',
    'whatweb' : 'dwhatweb:v1',
    'masscan' : 'dmasscan:v1',
    'dnsrecon' : 'ddnsrecon:v1',
    'gobuster' : 'dgobuster:v1'
}

# ANY
tools = [
    {
        'tool' : 'cewl',
        'image' : 'dcewl:v1',
        'params' : [''], # no parameters
        'parser' : 'parsers.cewl.cewlparse.parse_output'
    },
    {
        'tool' : 'whatweb',
        'image' : 'dwhatweb:v1',
        'params' : ['-a1'],
        'parser' : 'parsers.whatweb.whatwebparse.parse_output_basic'
    },
    {
        'identifier' : 'Shcheck_basic',
        'tool' : 'shcheck',
        'image' : 'dshcheck:v1',
        'service' : 'https',
        'params' : '', # no parameters
        'core' : 'cores.shcheck.shckech_core.run', 
        'parser' : 'parsers.shcheck.shcheckparse.parse_output'
    },
    {
        'tool' : 'nmap',
        'image' : 'dnmap:v1',
        'params' : ['-sn'], # ICMP Echo Request scan
        'parser' : 'parsers.nmap.nmapdiscoveryparse.parse_output'
    },
    {
        
        'identifier' : 'Nmap_ports_basic',
        'tool' : 'nmap',
        'image' : 'dnmap:v1',
        'service' : 'ANY',
        'params' : '-sS',
        'core' : 'cores.nmap.nmap_core.run', 
        'parser' : 'parsers.nmap.nmapparse.parse_output'
    },
    {
        'tool' : 'nmap',
        'image' : 'dnmap:v1',
        'params' : ['--script ssl-cert'],
        'parser' : 'parsers.nmap.nmapSSLparse.parse_output'
    },
    {
        'tool' : 'dnsrecon',
        'image' : 'ddnsrecon:v1',
        'params' : ['-t std'],
        'parser' : 'parsers.dnsrecon.dnsreconparse.parse_output'
    },
 {
        'tool' : 'dnsrecon',
        'image' : 'ddnsrecon:v1',
        'params' : ['-r'],
        'parser' : 'parsers.dnsrecon.dnsreverseparse.parse_output'
    },
    {
        'tool' : 'gobuster',
        'image' : 'dgobuster:v1',
        'params' : ['-k -q'],
        'parser' : 'parsers.gobuster.gobusterparse.parse_output'
    },
    {
        'tool' : 'masscan',
        'image' : 'dmasscan:v1',
        'params' : [''],
        'parser' : 'parsers.masscan.masscanparse.parse_output'
    }
    
]

modules = {
    # 'Nmap' : {},
    # 'Nmap' : {
    #     'tool' : 'nmap',
    #     'image' : 'dnmap:v1',
    #     'service' : 'ANY',
    #     'params' : '-sS', # no parameters
    #     'core' : 'cores.nmap.nmap_core.run', 
    #     'parser' : 'parsers.nmap.nmapparse.parse_output'
    # },
    'Shcheck_basic' : {
        'image' : 'dshcheck:v1',
        'service' : 'https',
        'params' : '-d', # disable SSL chceck
        'core' : 'cores.shcheck.shckech_core.run', 
        'parser' : 'parsers.shcheck.shcheckparse.parse_output'
    },
    'Whatweb' : {
        'image' : 'dwhatweb:v1',
        'service' : 'https',
        'params' : '-a1',
        'core' : 'cores.whatweb.whatweb_core.run',
        'parser' : 'parsers.whatweb.whatwebparse.parse_output_basic'

    },
    'Dnsrecon' : {
        'image' : 'ddnsrecon:v1',
        'service' : 'domain',
        'params' : '-t std',
        'core' : 'cores.dnsrecon.dnsrecon_cl.run',
        'parser' : 'parsers.dnsrecon.dnsreconparse.parse_output'
     } ,
    'Dnsrecon_reverse' : {
        'image' : 'ddnsrecon:v1',
        'service' : 'domain',
        'params' : '', # there is parameter '-r' which is hardcoded
        'core' : 'cores.dnsrecon.dnsrecon_rev.run',
        'parser' : 'parsers.dnsrecon.dnsreverseparse.parse_output'
    },
    'Cewl' : {
        'image' : 'dcewl:v1',
        'service' : 'https',
        'params' : '', # no parameters
        'core' : 'cores.cewl.cewl_core.run',
        'parser' : 'parsers.cewl.cewlparse.parse_output',
        'outputfile' : '/home/kali/Templates/out.txt'
    },
    'NmapSSL' : {
        'image' : 'dnmap:v1',
        'service' : 'https',
        'params' : '--script ssl-cert',
        'core' : 'cores.nmap.nmapssl.run',
        'parser' : 'parsers.nmap.nmapSSLparse.parse_output'
    },
    'Sslscan' : {
        'image' : 'dsslscan:v1',
        'service' : 'https',
        'params' : '--xml=-',
        'core' : 'cores.sslscan.sslscan_core.run',
        'parser' : 'parsers.sslscan.sslscanparse.parse_output'
    },
    'Gobuster' : {
        'image' : 'dgobuster:v1',
        'service' : 'https',
        'params' : '-k -q',
        'core' : 'cores.gobuster.gobuster_core.run',
        'parser' : 'parsers.gobuster.gobusterparse.parse_output',
        'wordlist' : 'common.txt'
    }
}