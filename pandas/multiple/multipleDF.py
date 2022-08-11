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

# Cool T-Shirts Inc.
sales = pd.read_csv('learningDS/pandas/multiple/sales.csv')
print(sales)

targets = pd.read_csv('learningDS/pandas/multiple/targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]

print(crushing_it)