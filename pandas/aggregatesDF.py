# Revisiting orders DataFrame

import pandas as pd

orders = pd.read_csv('learningDS/pandas/orders.csv')

print(orders.head(10))

most_expensive = orders.price.max()

print(most_expensive)

num_colors = orders.shoe_color.nunique()

print(num_colors)

# Using .groupby to calculate aggregates

pricey_shoes = orders.groupby('shoe_type').price.max()

print(pricey_shoes)

print(type(pricey_shoes))