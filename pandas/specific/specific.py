import pandas as pd

# Using rename for our merges 
orders = pd.read_csv('learningDS/pandas/specific/orders.csv')
print(orders)

customers = pd.read_csv('learningDS/pandas/specific/customers.csv')
print(customers)

products = pd.read_csv('learningDS/pandas/specific/products.csv')
print(products)

orders_vs_customers = pd.merge(
    orders,
    customers.rename(columns={'id':'customer_id'})
)
print(orders_vs_customers)

# Merge orders and products using .rename()
orders_products = pd.merge(
    orders,
    products.rename(columns={'id': 'product_id'})
)
print(orders_products)