import pandas as pd
import numpy as np

# Read NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census2.csv")

correct_order = ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)']

nyc_trees.tree_diam_category = pd.Categorical(nyc_trees.tree_diam_category, ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)'], ordered=True)

# Get Mean Diam of diameter variable, `trunk_diam`
mean_diam = nyc_trees.trunk_diam.mean()
print(mean_diam)

# Get Mean Category of `tree_diam_category`
mean_diam_cat = np.mean(nyc_trees['tree_diam_category'].cat.codes)
print(mean_diam_cat)
median_category = correct_order[int(mean_diam_cat)]
print(median_category)
