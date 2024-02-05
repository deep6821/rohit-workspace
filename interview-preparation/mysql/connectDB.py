'''-->>SELECT Database is used in MySQL to select a particular database to work with. This query is used when multiple databases are available with MySQL Server.
     we can use SQL command USE to select a particular database. '''

import MySQLdb as mydb,time
con = None
try:
        con = mydb.connect("localhost","root","tas123","pandey")
        print "Connected successfully"
        time.sleep(5)

except mydb.Error,e:
        print "Connect Eorror:%d,%s"%(e.args[0],e.args[1])
        exit(1)

finally:
        if con:
                con.close()
                print "Disconnnected Successfully"
exit(0)

