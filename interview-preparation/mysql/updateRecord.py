#-->>MySQL UPDATE statement is used to update data of the MySQL table within the database. It is used when you need to modify the table. 

import MySQLdb as mydb
import time
con = None

con = mydb.connect("localhost","root","tas123","pandey")
print "Connected successfully"
cur = con.cursor()
stmt = "update customer set cus_lastName = 'Sharma' where cus_id = %s" %(1)

try:
    cur.execute(stmt)
    con.commit()

except mydb.Error,e:
    print 'connect Error:%d,%s'%(e.args[0],e.args[1])
    exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"

exit(0)

