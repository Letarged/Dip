images = {
    'nmap' : 'dnmap:v1',
    'cewl' : 'dcewl:v1',
    'shcheck' : 'dshcheck:v1',
    'whatweb' : 'dwhatweb:v1',
    'masscan' : 'dmasscan:v1',
    'dnsrecon' : 'ddnsrecon:v1',
    'gobuster' : 'dgobuster:v1'
}

tools = [
    {
        'tool' : 'cewl',
        'image' : 'dcewl:v1',
        'params' : [''], # no parameters
        'parser' : 'parsers.cewl.cewlparser.parse_output'
    },
    {
        'tool' : 'whatweb',
        'image' : 'dwhatweb:v1',
        'params' : ['-a1'],
        'parser' : 'parsers.whatweb.whatwebparse.parse_output_basic'
    },
    {
        'tool' : 'nmap',
        'image' : 'dnmap:v1',
        'params' : ['-sn'],
        'parser' : ''
    }
]