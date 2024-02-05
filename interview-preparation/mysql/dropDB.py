'''-->>We can drop/delete/remove a MySQL database easily with the MySQL command. We should be careful while deleting any database because we will lose your all the data available in our database. '''

import MySQLdb as mydb
import time
con = None
try:
    con = mydb.connect('localhost','root','tas123','pandey')
    cur = con.cursor()
    cur.execute('DROP DATABASE ppp')
    print 'Deleted  successfully'
    time.sleep(5)

except mydb.Error,e:
    print 'connect Error:%d,%s'%(e.args[0],e.args[1])
    exit(1)

finally:
    if con:
        con.close()
        print "disconnected successfully"
exit(0)

