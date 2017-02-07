#!/usr/bin/python
__author__ = 'Ryan Tischer'

#FILENAME.py: Description of program or code.
#Use at your own risk
#Contact @ryantischer

import re

#todo
#make it work
#deal with different types of configurations
#nat pool

realServer = []
frontEnd = []
tmp = []

TA_Config = {
  "configs": [
    {
      "nat_subnet_pool": [
        "7.0.0.0/24",
        "7.0.0.0/24"
      ],
      "protocol": 6,
      "name": "Reporting NLB IPv4 Config",
      "vip": "7.0.0.50",
      "backends": [
        {
          "backend_port": 80,
          "backend_ip": "7.0.0.41"
        },
      ],
      "type": 2,
      "vip_port": 80
    }
  ]
}


bindAddress = ""
found = "False"

with open('haproxy.cfg', 'r') as searchfile:
    for line in searchfile:

        if found == "True":
         bindAddress = line
         found = "False"
        #find backend
        tmp = re.findall(r"server \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b.*",line)
        if tmp != []:
            realServer.append(tmp)
        #find frontEnd
        tmp = re.findall("^listen  haproxy_.*", line)
        if tmp != []:
            found = "True"
        tmp = re.findall("node haproxy.*", line)
        if tmp != []:
            frontEnd = tmp

len = len(realServer)

counter = 0
tmp={}

for i in realServer:

     #build the backends

    tmp["backend_ip"] = str(realServer[counter][0]).split(" ",4)[1]

    TA_Config["configs"][0]["backends"].append(tmp)

    tmp = str(realServer[0]).split(":",3)[1]

    #tmp = tmp.split(" ",2)
    #print tmp
    #tmp["backend_port"] = tmp[0]
    #print tmp



    counter = counter + 1



bindAddress = bindAddress.split(":",2)

#change the dict
TA_Config["configs"][0]["name"] = "haproxy import"
#TA_Config["configs"][0]["vip"] =

#get the IP out of the file.  Got to be a better way to do this
frontEnd = str(frontEnd)
tmp = frontEnd.split("_",2)
tmp2 = str(tmp[1])
tmp2 = tmp2.split("'",2)
TA_Config["configs"][0]["vip"] = tmp2[0]
TA_Config["configs"][0]["vip_port"] = bindAddress[1]

#for i in range(0,len - 1):
#    print realServer
#   print str(realServer[0][0]).split(" ",4)[1]
#TA_Config["configs"][0]["backends"][i][backend_ip] =
#print TA_Config
print TA_Config["configs"][0]["backends"][1]
print TA_Config["configs"][0]["backends"][0]