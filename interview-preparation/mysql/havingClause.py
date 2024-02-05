#-->> MySQL HAVING Clause is used with GROUP BY clause. It always returns the rows where condition is TRUE.

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    #cur.execute('select address, count(address) from officers group by address ')
    #cur.execute('select emp_name, sum(working_hours) as "Total working hours" from emp group by emp_name ')
    #cur.execute('select emp_name, min(working_hours) as "Minimum working hour" from emp group by emp_name ')
    #cur.execute('select emp_name, avg(working_hours) as "Average working hour" from emp group by emp_name ')
    cur.execute('select emp_name, sum(working_hours) as "Total working hours" from emp group by emp_name having sum(working_hours) > 5')
    data = cur.fetchall()
    for i in range(len(data)):
        print 'emp_name: ',data[i][0], "Total working hours: ", data[i][1]
        print "++++++++++++++++++++++++++++++++++++++++++++"

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    print exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"
