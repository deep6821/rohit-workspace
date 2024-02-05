# -->>MySQL INSERT statement is used to insert data in MySQL table within the database. We can insert single or multiple records using a single query in MySQL.i

import datetime
import MySQLdb as mydb
import time

con = None
con = mydb.connect('localhost', 'root', 'Rohit6821@', 'TT')
print('connected successfully')
cur = con.cursor()

query = '''
    insert into test(id, name, division_id, manager_id, salary) VALUES (133, 'Susan Wall', 105, 577, 110000);
'''

# Insert rows dynamically
field_names = [
    'employee_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'job_id', 'salary',
    'commission_pct', 'manager_id', 'department_id']

field_values = [
    100, 'steven', 'king', 'sking@gmail.com', '515.123.4567', datetime.datetime(1987, 6, 17).strftime("%Y-%m-%d"),
    'AD_PRES', 24000, 0.3, 3, 90]

query_columns = ', '.join(field_names)
query_placeholders = ', '.join(['%s'] * len(field_values))

query = ''' INSERT INTO employees (%s) VALUES (%s) ''' % (query_columns, query_placeholders)
try:
    # cur.execute(query)
    cur.execute(query, field_values)
    con.commit()

except Exception as e:
    print(e)
    exit(1)

finally:
    if con:
        con.close()
        print("disconnected successfully")
exit(0)
