'''-->> MySQL ALTER statement is used when you want to change the name of your table or any table field. It is also used to add or delete an existing column in a table.
The ALTER statement is always used with "ADD", "DROP" and "MODIFY" commands according to the situation.  '''

import MySQLdb as mydb
import time
con = None

#-->>1. ADD a column in the table
#-->>2. Add multiple columns in the table  
#-->>3. MODIFY column in the table 
try:
    con = mydb.connect("localhost","root","tas123","pandey")
    print "Connected successfully"
    cur = con.cursor()
    cur = con.cursor()
    #cur.execute('alter table customer add cur_avg varchar(40) NOT NULL')
    #cur.execute('alter table customer add(cus_address varchar(100) not null, cus_surname, cus_salary int(100) not null after cus_age)')
    cur.execute('alter table customer modify cus_lastName varchar(50) null')      

    ''''cur.execute('select * from customer')
    data = cur.fetchall()
    for i in range(len(data)):
        print 'cus_id:',data[i][0]
        print 'cus_firstName:',data[i][1]
        print 'cus_lastName:',data[i][2]
        print 'cur_avg:',data[i][3] '''

except mydb.Error,e:
    print 'Connect Error: %d,%s' %(e.args[0],e.args[1])
    exit(1)

finally:
    if con:
        con.close()
        print "Disconnected successfully"

exit(0)

#-->>2. Add multiple columns in the table   
 


