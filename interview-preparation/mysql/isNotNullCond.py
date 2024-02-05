#-->>MySQL IS NOT NULL condition is used to check the NOT NULL value in the expression. It is used with SELECT, INSERT, UPDATE and DELETE statements.
# Here, we are getting the complete "officers" table as result because every value is NOT NULL in the table. 

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    cur.execute('select * from officers where officer_name is not null')
    data = cur.fetchall()
    for i in range(len(data)):
        print 'officer_id: ',data[i][0]
        print 'officer_name: ',data[i][1]
        print 'officer_address: ',data[i][2]
        print "++++++++++++++++++++++++++++++++++++++++++++"

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    print exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"


