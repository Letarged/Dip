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
        'tool' : 'shcheck',
        'image' : 'dshcheck:v1',
        'params' : [''], # no parameters
        'parser' : 'parsers.shcheck.shcheckparse.parse_output'
    },
    {
        'tool' : 'nmap',
        'image' : 'dnmap:v1',
        'params' : ['-sn'], # ICMP Echo Request scan
        'parser' : 'parsers.nmap.nmapdiscoveryparse.parse_output'
    },
    {
        'tool' : 'nmap',
        'image' : 'dnmap:v1',
        'params' : ['-sS'],
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