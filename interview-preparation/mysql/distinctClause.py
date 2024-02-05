#-->>MySQL DISTINCT clause is used to remove duplicate records from the table and fetch only the unique records. The DISTINCT clause is only used with the SELECT statement. 

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    #cur.execute('select * from officers') 
    #cur.execute('select distinct address from officers') 
    cur.execute('select distinct officer_name, address from officers') 
    data = cur.fetchall()
    for i in range(len(data)):
        print 'officer_name: ',data[i][0]
        print 'officer_address: ',data[i][1]
        print "++++++++++++++++++++++++++++++++++++++++++++"

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    print exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"

