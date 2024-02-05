'''-->>MySQL JOINS are used with SELECT statement. It is used to retrieve data from multiple tables. It is performed whenever you need to fetch records from two or more tables.

There are three types of MySQL joins:
    MySQL INNER JOIN (or sometimes called simple join)
    MySQL LEFT OUTER JOIN (or sometimes called LEFT JOIN)
    MySQL RIGHT OUTER JOIN (or sometimes called RIGHT JOIN) '''

import MySQLdb as mydb
import time
con = None

try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    #cur.execute('select s.id, s.student_name, c.course_name from student s join course c on s.id = c.id ') 
    #cur.execute('select s.id, s.student_name, c.course_name from student s left join course c on s.id = c.id ') 
    cur.execute('select s.id, s.student_name, c.course_name from student s right join course c on s.id = c.id ') 
    data = cur.fetchall()
    for i in range(len(data)):
            print 'student_id : ',data[i][0]
            print 'student_name, : ',data[i][1]
            print 'c.course_name : ',data[i][2]
            print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

except mydb.Error,e:
    print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
    exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"



