import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

# Manufacturer Country
manufacturer_country_counts = car_eval.manufacturer_country.value_counts()
print(manufacturer_country_counts)

fourth_manufacturer_country = manufacturer_country_counts.index[3]
print(fourth_manufacturer_country)

manufacturer_country_proportions = car_eval.manufacturer_country.value_counts(normalize=True)
print(manufacturer_country_proportions.head())

# Buying Cost
print(car_eval.buying_cost.unique())

buying_cost_categories = ['low', 'med', 'high', 'vhigh']

car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered=True)

buying_cost_median = np.median(car_eval['buying_cost'].cat.codes)

print(buying_cost_median)

# Luggage
luggage_proportions = car_eval.luggage.value_counts(dropna=False, normalize=True)

print(luggage_proportions)

# Doors
Five_or_more_frequency = (car_eval['doors'] == ('5more')).sum()
print(Five_or_more_frequency)

Five_or_more_proporcion = (car_eval['doors'] == ('5more')).mean()
print(Five_or_more_proporcion)
