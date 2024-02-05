#-->>MYSQL DROP table statement removes the complete data with structure. 

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pndey")
    print "Connected successfully"
    cur = con.cursor() 
    cur.execute('drop table customer')

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    exit(1)

finally:
    if con:
        print "Disconnected successfully"
        
exit(0)    
