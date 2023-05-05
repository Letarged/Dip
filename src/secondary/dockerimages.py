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
        'tool' : 'shcheck',
        'image' : 'dshcheck:v1',
        'service' : 'https',
        'params' : '-d', # disable SSL chceck
        'core' : 'cores.shcheck.shckech_core.run', 
        'parser' : 'parsers.shcheck.shcheckparse.parse_output'
    },
    'Whatweb' : {
        'tool' : 'whatweb',
        'image' : 'dwhatweb:v1',
        'service' : 'https',
        'params' : '-a1',
        'core' : 'cores.whatweb.whatweb_core.run',
        'parser' : 'parsers.whatweb.whatwebparse.parse_output_basic'

    }
}