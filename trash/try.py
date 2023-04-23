#!/usr/bin/python3

from urllib.parse import urlparse
import ipaddress

def check_ip_or_url(value):

    try:
        ip = ipaddress.ip_address(value)
        return "ip"
    except:
        return "url"


x = "https://whiskeyprovsechny.cz"
print(check_ip_or_url(x))