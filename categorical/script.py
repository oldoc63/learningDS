import pandas as pd
import numpy as np

# Read NYC trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Find the unique values in the column health
tree_health_statuses = nyc_trees.health.unique()
print(tree_health_statuses)

#Create a list named health_categories which lists the categories from worst to best. Exclude NaN.
health_categories = ['Poor', 'Fair', 'Good']

#convert health to 'category'
nyc_trees['health'] = pd.Categorical(nyc_trees['health'], health_categories, ordered=True)

#calculate the median value of health
median_index = np.median(nyc_trees['health'].cat.codes)
print(median_index)
median_health_status = health_categories[int(median_index)]
print(median_health_status)



