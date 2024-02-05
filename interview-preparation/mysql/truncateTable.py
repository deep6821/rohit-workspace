'''-->>MYSQL TRUNCATE statement removes the complete data without removing its structure. The TRUNCATE TABLE statement is used when you want to delete the 
complete data from a table without removing the table structure. '''

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pndey")
    print "Connected successfully"
    cur = con.cursor()
    cur.execute('truncate table customer')

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    exit(1)

finally:
    if con:
        print "Disconnected successfully"

exit(0)

