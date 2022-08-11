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

# Each DataFrame has its own .merge() method
new_df = orders.merge(customers)

# We can chain the commands
big_df = orders.merge(customers).merge(products)

print(big_df)

# men_women_sales.csv
men_women = pd.read_csv('learningDS/pandas/multiple/men_women_sales.csv')

# Merge all three DataFrames (sales, targets and men_women)
all_data = sales.merge(targets).merge(men_women)

print(all_data)

# Do they have more revenue in months where they sell more women t-shirts
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

print(results)