-- Combining tables
SELECT *
FROM orders
JOIN customers
ON orders.customer_id = customers-customer_id;

-- table_name.column_name syntax
SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;

-- Adding WHERE statement after ON
SELECT *
FROM orders
JOIN subscriptions
  ON orders.subscription_id = subscriptions.subscription_id
WHERE subscriptions.description = 'Fashion Magazine';

-- Use COUNT to count all the rows of a table
SELECT COUNT(*)
FROM newspaper;

SELECT COUNT(*)
FROM online;

-- JOIN newspaper and online tables on id
SELECT COUNT(*)
FROM newspaper
JOIN online
ON newspaper.id = online.id;

-- LEFT JOIN keep all rows of the first table but will omit the un-matched row from the second table
SELECT *
FROM table1
LEFT JOIN table2
ON table1.c2 = table2.c2;

-- How many users subscribe to the print newspaper, but not to the online.
SELECT *
FROM newspaper
LEFT JOIN online
ON newspaper.id = online.id
WHERE online.id IS NULL;

--Perform an inner join of classes and students using the primary and foreign keys described above, and select all the colums
SELECT *
FROM classes
JOIN students
ON classes.id = students.class_id;

-- CROSS JOIN don't require an ON statement
SELECT shirts.shirt_color, pants.pant_color
FROM shirts
CROSS JOIN pants;

-- Count the number of customers who were subscribed to the newspaper during March.
SELECT COUNT(*)
FROM newspaper
WHERE start_month <= 3
AND end_month >= 3

-- Select all the columns from the cross join of newspaper and months
SELECT *
FROM newspaper
CROSS JOIN months;

-- Create a third query where you add a WHERE statement to your cross join to restrict to two conditions
SELECT *
FROM newspaper
CROSS JOIN months
WHERE start_month <= month
AND end_month >= month
GROUP BY month;

-- Combine two tables using UNION
SELECT *
FROM table1
UNION
SELECT *
FROM table2;

-- Tables must have the same number of columns
-- Tables must have the same data types in the same order

SELECT *
FROM newspaper
UNION
SELECT *
FROM online;

-- How many magazines each customer subscribe to
SELECT customer_id,
COUNT(subscription_id) AS 'subscriptions'
FROM orders
GROUP BY customer_id;

-- Using the WITH statement
WITH previous_query AS (
  SELECT customer_id,
    COUNT(subscription_id) AS 'subscriptions'
  FROM orders
  GROUP BY customer_id
)
SELECT customers.customer_name,
    previous_query.subscriptions
FROM previous_query
JOIN customers
  ON previous_query.customer_id 
  = customers.customer_id;