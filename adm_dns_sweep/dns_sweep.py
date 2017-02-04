#!/usr/bin/python
__author__ = 'Ryan Tischer'

#dns_sweep.py: Description of program or code.
#Use at your own risk
#Contact @ryantischer
'''
dns_sweep.py sweeps an address range and builds a hostname to IP address map file.  dns_sweep.py uses the hosts DNS
settings.  The input is any valid IP address, and will scan all address in the /24 subnet.
 THe output is a json formated file that is compatilibe with top secert Cisco analytics tools.
'''

import socket
import sys
import json

#check input

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print "invalid input...Usage is 'python dns_sweep.py IPADDRESS.  THe script scans everything in the /24 subnet exiting"
    sys.exit()

ipAddrStart = sys.argv[1]


try:
    socket.inet_aton(ipAddrStart)
    # legal
except socket.error:
    print "IP address is not valid.  Exiting..."
    sys.exit()
    # Not legal

#end check input


#split the IP address string into octets.
ipOctet = ipAddrStart.split(".")

#build empty dictonary file
file={}

#This for loop runs throught the subnet and uses socket.gethostbyaddr to find the hostmane by IP.  Data is stored in
#a Python dictonary.

for i in xrange(1,254):
    workingIP = ipOctet[0] + "." + ipOctet[1] +"." + ipOctet[2] + "." + str(i)
    try:
        node = socket.gethostbyaddr(workingIP)
        hostname = node[0]
        hostIP = json.dumps(node[2])
        hostIP = hostIP[2:-2]
        file [hostIP] = hostname
    except:
        print workingIP + " has no DNS record"

'''
Example data

{
 "10.0.0.1": "host-1.example.com",
 "10.0.0.2": "host-2",
 "10.0.0.3": "host 3"
 }

'''

#dump the file
with open('dns_data.json', 'w') as outfile:
     json.dump(file, outfile, sort_keys = True, indent = 4,
ensure_ascii=False)


print "The file dns_data.json is ready for import"