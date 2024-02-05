# -->>The MySQL SELECT statement is used to fetch data from the one or more tables in MySQL. We can retrieve records of all fields or specified fields.

import MySQLdb as mydb
import time

con = None

try:
    con = mydb.connect("localhost", "root", "Rohit6821@", "TT")
    print("Connected successfully")
    cur = con.cursor()
    # 3rd highest salary
    N = 3
    query = '''
        SELECT * FROM test t1 WHERE 3-1 = (SELECT COUNT(DISTINCT salary) FROM test t2 WHERE t2.salary > t1.salary);
    '''

    # query = '''
    #     SELECT TOP 1 salary FROM(SELECT DISTINCT TOP 3 salary FROM test ORDER BY salary DESC) AS temp ORDER BY salary;
    # '''


    # query = '''
    #     SELECT a.id AS "ID", a.name AS "Name", b.id AS "Manager ID", b.name AS "Manager Name"
    #     FROM test a, test b WHERE a.manager_id = b.id;
    # '''

    cur.execute(query)
    data = cur.fetchall()
    print("Data --->>", data)
    # for i in data:
    #     print("+++++++++++++++++++++++++++++++++++++")
    #     print("Id: ", i[0])
    #     print("Name: ", i[1])
    #     print("Division Id: ", i[2])
    #     print("Manager Id: ", i[3])
    #     print("Salary: ", i[4])




except Exception as e:
    print(e)
    exit(1)

finally:
    if con:
        con.close()
        print("Disconnected successfully")

exit(0)
