#-->>MySQL WHERE Clause is used with SELECT, INSERT, UPDATE and DELETE clause to filter the results. It specifies a specific position where you have to do the operation

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    #cur.execute('select * from officers where address = "Nagpur" ')
    #cur.execute('select * from officers where address = "Pune" and officer_id < 5 ')
    #cur.execute('select * from officers where address = "Pune" or address = "Bhopal" ')
    cur.execute('select * from officers where (address = "Bhopal" and officer_name = "Rohit") or (officer_id < 5)')
    data = cur.fetchall()
    for i in range(len(data)):
        print 'officer_id: ',data[i][0]
        print 'officer_name: ',data[i][1]
        print 'officer_address: ',data[i][2]

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    print exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"

exit(0)

