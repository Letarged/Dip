#!/usr/bin/python3

def not_forbidden(forbidden_list, interface):
    if len(interface) == 2:
        if interface in forbidden_list:
            return False
    else:
        if (interface in forbidden_list) or (interface[:(len(interface)-1)] in forbidden_list):
            return False
            
    return True


forb = ['lo', 'eth', 'wlan', 'docker']

my_interface = "docker0"

if not_forbidden(forb, my_interface):
    print("ALLOWED")
else:
    print("FORBIDDEN")