'''-->>In MySQL, View is a virtual table created by a query by joining one or more tables. 
A VIEW is created by SELECT statements. SELECT statements are used to take data from the source table to make a VIEW. '''

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    #cur.execute('create view trainer as select cus_firstName,cus_lastName from customer')
    cur.execute('select * from trainer') #-->>To see the created VIEW:
    data = cur.fetchall()
    for i in range(len(data)):
        print 'cus_firstName:',data[i][0]
        print 'cus_lastName:',data[i][1]

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    exit(1)

finally:
    if con:
        print "Disconnected successfully"

exit(0)

