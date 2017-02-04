#!/usr/bin/python
__author__ = 'Ryan Tischer'

#FILENAME.py: Description of program or code.
#Use at your own risk
#Contact @ryantischer

import re

#http://stackoverflow.com/questions/4785244/search-a-text-file-and-print-related-lines-in-python

realServer = []
frontEnd = []
tmp = []

TA_Config = {
 "configs": [
  {
   "name": "Example name for IPv4 config",
   "vip": "10.1.85.14",
   "vip_port": 3306,
   "protocol": 6,
   "backends": [
    {
     "backend_ip": "10.1.85.11",
     "backend_port": 3306
    },
    {
     "backend_ip": "10.1.85.12",
     "backend_port": 3306
    },
    {
     "backend_ip": "10.1.85.13",
     "backend_port": 3306
    }
   ],
   "nat_subnet_pool": [
    "0.0.0.0/0",
    "0.0.0.0/0"
   ]
  },
  {
   "name": "Example name for IPv6 config",
   "vip": "fe80::",
   "vip_port": 80,
   "protocol": 6,
   "backends": [
    {
     "backend_ip": "fe80:0001::",
     "backend_port": 80
    },
    {
     "backend_ip": "fe80:0002::",
     "backend_port": 80
    },
    {
     "backend_ip": "fe80:0003::",
     "backend_port": 80
    }
   ],
   "nat_subnet_pool": [
    "fe80::/16"
   ]
  }
 ]
}

with open('haproxy.cfg', 'r') as searchfile:
    for line in searchfile:
        #find backend
        tmp = re.findall(r"server \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b.*",line)
        if tmp != []:
            realServer.append(tmp)
        #find frontEnd
        tmp = re.findall("^listen  haproxy_.*", line)
        if tmp != []:
            frontEnd = tmp


print frontEnd
#print TA_Config["configs"][0]['vip']
#print TA_Config["configs"][0]['backends'][0]
for i in realServer:
 tmp = realServer[0]
 
 print tmp

