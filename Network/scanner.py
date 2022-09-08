#!/bin/python3

import sys, socket
from datetime import datetime

#define our target 
if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1]) #translate hosname to IPv4
else:
    print("Invalid amount of arguments")
    print("Syntax: Python3 scanner.py <IP>")

#add banner 
print("-"*50)
print("Scanning target " + target)
print("Time Started" + str(datetime.now()))
print("-"*50)

try: 
    for port in (50,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # wait 1 second and move on 
        result = s.connect_ex((target,port)) # port open => 0 , else 1 with an error indicateur 
        if result == 0: 
            print("Port {} is open ".format(port)) 
        s.close
except KeyboardInterrupt:
    print("\n Exiting the program. ")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()