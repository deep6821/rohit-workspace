#-->>MySQL DELETE statement is used to delete data from the MySQL table within the database. By using delete statement, we can delete records on the basis of conditions.

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    cur.execute('delete from customer where cus_id = 2')

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    print exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"

exit(0)
   
