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