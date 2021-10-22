import pandas as pd
import numpy as np

# Get NYC Trees Data
nyc_trees = pd.read_csv('nyc_tree_census.csv')

# Frequency and proportion of trees that were recorded as Alive
living_frequency = np.sum(nyc_trees.status == 'Alive')
living_proportion = (nyc_trees.status == 'Alive').mean()
print(living_frequency)
print(living_proportion)

# Find the frequency and proportion of trees with trunk_diam > 30
giant_frequency = np.sum(nyc_trees.trunk_diam > 30)
giant_proportion = (nyc_trees.trunk_diam > 30).mean()
print(giant_frequency)
print(giant_proportion)

