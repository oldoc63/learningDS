import pandas as pd

orders = pd.read_csv('learningDS/pandas/mismatch/orders.csv')
print(orders)

products = pd.read_csv('learningDS/pandas/mismatch/products.csv')
print(products)

merge_df = orders.merge(products)

print(merge_df)