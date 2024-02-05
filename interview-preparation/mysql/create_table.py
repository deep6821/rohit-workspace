import MySQLdb as mydb
import time

con = None

try:
    con = mydb.connect("localhost", "root", "Rohit6821@", "TT")
    print("Connected successfully")
    cur = con.cursor()
    # query = '''create table emp
    #     emp_id int not null auto_increment,
    #     emp_name VARCHAR(100) NOT NULL,
    #     working_date date,
    #     working_hours time,
    #     primary key(emp_id, working_date)
    # '''

    query = '''create table test(
        id int not null,
        name char(20),
        division_id int,
        manager_id int,
        salary int
    )'''

    query = '''create table employees(
        employee_id int not null primary key,
        first_name varchar(20) not null,
        last_name varchar(20) not null,
        email varchar(20) default null,
        phone_number varchar(20) default null,
        hire_date date default null,
        job_id varchar(20) not null, 
        salary int not NULL,
        commission_pct decimal(2,2) default null,
        manager_id int not null,
        department_id int not null
    )'''
    cur.execute(query)

except Exception as e:
    print(e)
    exit(1)

finally:
    if con:
        con.close()
        print("Disconnected successfully")

exit(0)
