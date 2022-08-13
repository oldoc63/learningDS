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

# Merge orders and customers using left_on and rigth_on
pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id'
)