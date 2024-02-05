import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","Rohit6821@")
    cur = con.cursor()
    cur.execute('create database db_test')
    print "Database created successfully"

except mydb.Error, e:
    print 'connect Error:%d,%s'%(e.args[0],e.args[1]) 
    exit(1)

finally:
    if con:
        con.close()
        print "disconnected successfully"

exit(0)


def resetdb(self):
    self.db = {}
    self.dumpdb()
    return True