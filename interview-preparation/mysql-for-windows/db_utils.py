import datetime
import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Rohit6821@"
MYSQL_DATABASE = "rohit_dev"


class MySQL:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.create_database_connection()

    def create_database_connection(self):
        try:
            self.connection = mysql.connector.connect(
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                host=MYSQL_HOST,
                database=MYSQL_DATABASE
            )
            self.cursor = self.connection.cursor()
        except Exception as error:
            print("Exception: ", error)

    def create_table(self):
        try:
            query = '''create table customer(
                customer_id int not null primary key,
                name varchar(20) default null,
                age int default null,
                address varchar(40) default null,
                salary int default null
            )'''
            query = '''create table orders(
                order_id int not null primary key,
                customer_id int not null,
                date datetime default null,
                amount int default null
            )'''
            self.cursor.execute(query)
        except Exception as error:
            print("Exception: ", error)

    def insert_records(self):
        # Insert rows dynamically
        field_names = ['customer_id', 'name', 'age', 'address', 'salary']
        field_value_list = [
            [1, 'Mark', 32, 'Texas', 50000],
            [2, 'John', 25, 'NY', 65000],
            [3, 'Emily', 23, 'Ohio', 20000],
            [4, 'Bill', 25, 'Chicago', 75000],
            [5, 'Tom', 27, 'Washington', 35000],
            [6, 'Jane', 22, 'Texas', 45000],

        ]

        field_names = ['order_id', 'customer_id', 'date', 'amount']
        field_value_list = [
            [100, 2, datetime.datetime(2019, 9, 8), 5000],
            [101, 5, datetime.datetime(2019, 8, 20), 3000],
            [102, 1, datetime.datetime(2019, 5, 12), 1000],
            [103, 2, datetime.datetime(2019, 2, 2), 2000]

        ]

        for field_values in field_value_list:
            query_columns = ', '.join(field_names)
            query_placeholders = ', '.join(['%s'] * len(field_values))
            query = ''' INSERT INTO orders (%s) VALUES (%s) ''' % (query_columns, query_placeholders)
            self.cursor.execute(query, field_values)
            self.connection.commit()

    def select_query(self):
        idx = [100]
        query = '''select customer_id, date from orders where order_id IN {};'''.format(tuple(idx))
        print(query)
        # query = query.replace(',)', ')')
        # print(query)
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)


if __name__ == "__main__":
    db_obj = MySQL()
    # db_obj.create_table()
    # db_obj.insert_records()
    db_obj.select_query()
