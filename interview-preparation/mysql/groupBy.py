'''#-->>The MYSQL GROUP BY Clause is used to collect data from multiple records and group the result by one or more column. It is generally used in a SELECT statement.
We can also use some aggregate functions like COUNT, SUM, MIN, MAX, AVG etc. on the grouped column. '''

#1- MySQL GROUP BY Clause with COUNT function

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
    cur.execute('select emp_name, avg(working_hours) as "Average working hour" from emp group by emp_name ')
    data = cur.fetchall()
    for i in range(len(data)):
        #print 'address: ',data[i][0], ":", data[i][1]
        #print 'emp_name: ',data[i][0], "Total working hours: ", data[i][1]
        #print 'emp_name: ',data[i][0], "Minimum working hour: ", data[i][1]
        #print 'emp_name: ',data[i][0], "Maximum working hour: ", data[i][1]
        print 'emp_name: ',data[i][0], "Average working hour: ", data[i][1]
        print "++++++++++++++++++++++++++++++++++++++++++++"

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    print exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"
