import pandas as pd

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