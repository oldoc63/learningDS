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

# Merge orders and customers using left_on and rigth_on and suffixes
rightON_leftON = pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
    suffixes=['_order', '_customer']
)
print(rightON_leftON)

# Merge orders and products using left_on and right_on
# Use suffixes _orders and _products
orders_products = pd.merge(
    orders,
    products,
    left_on='product_id',
    right_on='id',
    suffixes=['_order', '_product']
)
print(orders_products)