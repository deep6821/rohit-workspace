#-->>The MYSQL BETWEEN condition specifies how to retrieve values from an expression within a specific range. It is used with SELECT, INSERT, UPDATE and DELETE statement.

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    #cur.execute('select * from officers where officer_id between 1 and 3')
    cur.execute('select * from emp where working_date between cast("2016-03-08" as date) and cast("2016-03-09" as date)')
    data = cur.fetchall()
    for i in range(len(data)):
        print 'emp_id: ',data[i][0]
        print 'emp_name: ',data[i][1]
        print 'working_date: ',data[i][2]
        print 'working_hours: ',data[i][3]
        print "++++++++++++++++++++++++++++++++++++++++++++"

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    print exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"

