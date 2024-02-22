"""
You are given an SQL table containing changes in prices of 
articles in a shop of following structures:

Table: price_updates

Input 1:
-------
product           | date       | price
banana [single]   | 2020-01-21 | 1
banana [single]   | 2020-01-22 | 2
cheese            | 2020-01-23 | 1
potatoes [pack]   | 2020-01-21 | 3
potatoes [pack]   | 2020-01-30 | 3

Output 1:
--------
| product | 
  banana [single] 

Input 2:
-------
product      | date       | price
board game   | 2021-03-31 | 10
board game   | 2021-04-05 | 15
board game   | 2021-04-10 | 12
book         | 2021-03-31 | 10
book         | 2021-04-05 | 15
T-shirt      | 2021-03-31 | 10
T-shirt      | 2021-04-05 | 15

Output 2:
--------
| product | 
  board game  

Write an SQL query which lists all articles whose price increased 
with every update.

Note: The price of "cheese" was entered only once, so there was 
not enough data to determine whether it was increasing.
"""

"""
SELECT DISTINCT p1.product
FROM price_update p1
JOIN price_update p2 ON p1.product = p2.product
WHERE p1.date < p2.date
  AND p1.price < p2.price
  AND NOT EXISTS (
    SELECT 1
    FROM price_update p3
    WHERE p1.product = p3.product
      AND p1.date < p3.date
      AND p3.date < p2.date
      AND p1.price >= p3.price
      AND p3.price < p2.price
  );

"""