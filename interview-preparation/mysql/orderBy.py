#-->>The MYSQL ORDER BY Clause is used to sort the records in ascending or descending order. 

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    #cur.execute('select * from officers where address = "Bhopal" order by officer_name ')
    #cur.execute('select * from officers where address = "Bhopal" order by officer_name asc ')
    #cur.execute('select * from officers where address = "Bhopal" order by officer_name desc ')
    cur.execute('select officer_name, address from officers where officer_id < 5  order by officer_name desc, address asc ')
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


