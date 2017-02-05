#!/usr/bin/python
__author__ = 'Ryan Tischer'

#draw_ta.py: Description of program or code.
#Use at your own risk
#Contact @ryantischer
 
import json
import xlsxwriter

with open('Mirantis Openstack CMP-v18-policies.json') as f:
    a = f.read()
    jsondata = json.loads(a)

print jsondata['name']
#print jsondata['clusters'][0]['nodes']

#get all clusters and store in a list
clusterList= []

clusterData= {}

#Top for loop counter
tcounter = 0

#build the clusters

for clusters in jsondata['clusters']:

    clusterList.append (clusters['name'])
    currentCluster = clusters['name']
    #Bottom for loop counter
    bcounter = 0

    #init a list to holp node data
    z = []

    for nodes in jsondata['clusters'][tcounter]['nodes']:

        z.append([jsondata['clusters'][tcounter]['nodes'][bcounter]['ip'],jsondata['clusters'][tcounter]['nodes'][bcounter]['name']])

        clusterData[currentCluster] = z

        bcounter = bcounter + 1

    tcounter = tcounter + 1


# Create a workbook and add a worksheet.

workbook = xlsxwriter.Workbook('TA_ADM.xlsx')
worksheet = workbook.add_worksheet('Clusters')
worksheet.set_column(0, 0, 30)   # Column  A   width set to 20.
worksheet.set_column(1, 10, 15)   # Column  A   width set to 20.

row = 0
col = 0

for item in clusterData:
    if item != 'unknown':
        worksheet.write(row, col,item)
        #un comment to  print clusters
        #print item
        counter = 0

        for node in clusterData[item]:
            n = node[counter]
            worksheet.write(row, col + 1,n)
            col = col +1
        counter = counter + 1
        col = 0
        row = row + 1


#build the policys

#build the workbook
worksheet1 = workbook.add_worksheet('Policys')
worksheet1.set_column(0, 0, 30)   # Column  A   width set to 20.



row = 1
col = 1

#init var used in nested for loops
tcounter = 0
bcounter = 0
p = []

#loop through all policies in ADM file
for nodes in jsondata['policies']:
        #write src to the row, dst to the column
      n = (nodes['src_name'])
      worksheet1.write(row, 0,n)
      n = (nodes['dst_name'])
      worksheet1.write(0, col,n)

      bcounter = 0
      p =[]

      #loop though ports for each policy
      for ports in jsondata['policies'][tcounter]['whitelist']:

        p.append(ports['port'][0])

        bcounter = bcounter + 1
        #write to the worksheet
      worksheet1.write(row, col,str(p))

      #figure out the column len to set column size
      colLen = len(str(p))
        #set the col size
      worksheet1.set_column(col, col, colLen + 8)
      row = row + 1
      col = col +1
      tcounter = tcounter +1

workbook.close()

