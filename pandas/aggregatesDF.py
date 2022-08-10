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

#DataFrame teas
teas = pd.DataFrame([
    [0, 'earl grey', 'black', 38, 3],
    [1, 'english breakfast', 'black', 41, 3],
    [2, 'irish breakfast', 'black', 37, 2.5],
    [3, 'jasmine', 'green', 23, 4.5],
    [4, 'matcha', 'green', 48, 5],
    [5, 'camomile', 'green', 0, 3]
    ],
    columns=['id', 'tea', 'category', 'caffeine', 'price'])