"""
A JOIN clause is used to combine rows from two or more tables, based on a common column.


Notice that the CUSTOMER_ID in the ORDER table references ID in the CUSTOMER table.
Now, what if we need to query something that is the combination of information in both tables?

For example, we want to:
1. Find information on customers who ordered an item.
2. Find the number of customers who ordered a certain item.
3. Find the address of a customer in order to dispatch the order.
4. The joins in SQL can help you do that using the JOIN clause.

Different types of SQL JOINs:
-----------------------------
Here are the three different types of the JOINs we will be discussing in this chapter:

1. INNER JOIN / JOIN: Returns records that have matching values in both tables.
    Note: The INNER JOIN keyword selects all rows from both tables as long as there is a match between the columns. If
    there are records in the “Orders” table that do not have matches in “Customers”, these orders will not be shown.

2. LEFT JOIN/ LEFT OUTER JOIN: Returns all records from the left table, and the matched records from the right table
    Note: The LEFT JOIN keyword returns all records from the left table (table1), and the matched records from the right
    table (table2). The result is NULL from the right side if there is no match. In some databases, LEFT JOIN is called
    LEFT OUTER JOIN.

3. RIGHT JOIN/ RIGHT OUTER: Returns all records from the right table, and the matched records from the left table.
    Note: The RIGHT JOIN keyword returns all records from the right table (table2), and the matched records from the
    left table (table1). The result is NULL from the left side when there is no match. In some databases, RIGHT JOIN
    is called RIGHT OUTER JOIN.
"""
from db_utils import MySQL

database_object = MySQL()

inner_join_query = """ 
SELECT  customer.customer_id, customer.name, orders.amount, orders.date
FROM customer
INNER JOIN orders
ON customer.customer_id = orders.customer_id;"""

database_object.cursor.execute(inner_join_query)
inner_join_query_result = database_object.cursor.fetchall()
print(inner_join_query_result)

left_join_query = """
SELECT  customer.customer_id, customer.name, orders.amount, orders.date
FROM customer
LEFT JOIN orders
ON customer.customer_id = orders.customer_id
ORDER BY customer.customer_id;"""

database_object.cursor.execute(left_join_query)
left_join_query_result = database_object.cursor.fetchall()
print(left_join_query_result)

right_join_query = """
SELECT  customer.customer_id, customer.name, orders.amount, orders.date
FROM customer
RIGHT JOIN orders
ON customer.customer_id = orders.customer_id;"""

database_object.cursor.execute(right_join_query)
right_join_query_result = database_object.cursor.fetchall()
print(right_join_query_result)
