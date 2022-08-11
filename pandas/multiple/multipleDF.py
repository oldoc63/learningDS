import pandas as pd

orders = pd.read_csv('learningDS/pandas/multiple/orders.csv')

products = pd.read_csv('learningDS/pandas/multiple/products.csv')

customers = pd.read_csv('learningDS/pandas/multiple/customers.csv')

print(orders)

print(products)

print(customers)

# Inner Merge
new_df = pd.merge(orders, customers)

print(new_df)