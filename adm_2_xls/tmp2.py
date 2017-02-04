#!/usr/bin/python
#tmp file - do not use

__author__ = 'Ryan Tischer'

from numpy import *
import json
import xlsxwriter



#FILENAME.py: Description of program or code.
#Use at your own risk
#Contact @ryantischer


adm_policy = [['web_d','app_d','db_d'],
              ['web','0','1','0'],
              ['app','1','0','1'],
              ['db','0','1','0']]

with open('Mirantis Openstack CMP-v18-policies.json') as f:
    a = f.read()
    jsondata = json.loads(a)

data_matrix = [['Country', 'Year', 'Population'],
               ['United States', 2000, 282200000],
               ['Canada', 2000, 27790000],
               ['United States', 2005, 295500000],
               ['Canada', 2005, 32310000],
               ['United States', 2010, 309000000],
               ['Canada', 2010, 34000000]]


adm_policy.append(['dhcp','1','1','1'])

#print adm_policy

clusterList = [u'external-dns', u'external-to-dc', u'infosec', u'mcast-net', u'mos-compute-priv-tier', u'mos-compute-pub-tier', u'mos-compute-stor-tier', u'mos-controllers-priv-tier', u'mos-controllers-pub-tier', u'mos-controllers-stor-tier', u'mos-dfgw-tier', u'mos-fuel-master', u'mos-fuel-slaves', u'mos-horizon-pub-tier', u'mos-slb-priv-tier', u'mos-storage-priv-tier', u'mos-storage-pub-tier', u'mos-storage-stor-tier', u'mos-vrouter-controller', u'tetration-platform-tier']
len = len(clusterList)


#policyMatrix = array(range(len*len), dtype=object).reshape(len,len)
#policyMatrix.fill(0)

workbook = xlsxwriter.Workbook('TA_ADM2.xlsx')

worksheet1 = workbook.add_worksheet('Policys')
worksheet1.set_column(0, 0, 30)   # Column  A   width set to 20.
worksheet1.set_column(1, 10, 8)   # Column  b-fuck   width set to 20.

print jsondata['policies'][0]['whitelist'][0]['port'][0]

row = 1
col = 1


tcounter = 0
bcounter = 0

for nodes in jsondata['policies']:
      n = (nodes['src_name'])
      worksheet1.write(row, 0,n)
      n = (nodes['dst_name'])
      worksheet1.write(0, col,n)
      for ports in jsondata['policies'][tcounter]['whitelist']:
        n = ""
        n = str(n) + str(jsondata['policies'][tcounter]['whitelist'][0]['port'][bcounter])
        print n
        worksheet1.write(row, col,n)
        bcounter = bcounter + 1


      row = row + 1
      col = col +1
      tcounter = tcounter +1
workbook.close()


