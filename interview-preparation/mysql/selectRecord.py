# #-->>The MySQL SELECT statement is used to fetch data from the one or more tables in MySQL. We can retrieve records of all fields or specified fields.
#
# import MySQLdb as mydb
# import time
# con = None
#
# try:
#     con = mydb.connect("localhost","root","tas123","pandey")
#     print "Connected successfully"
#     cur = con.cursor()
#     #cur.execute('select cus_firstName,cus_lastName from customer')
#     cur.execute('select * from customer')
#     data = cur.fetchall()
#     for i in range(len(data)):
#             print 'cus_id : ',data[i][0]
#             print 'cus_firstName : ',data[i][1]
#             print 'cus_lastName : ',data[i][2]
#
# except mydb.Error,e:
#     print 'Connection Error: %d,%s' %(e.args[0],e.args[1])
#     exit(1)
#
# finally:
#     if con:
#         con.close()
#         print "Disconnected successfully"
#
# exit(0)
