import pandas as pd

# Read NYC Trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Table of proportions for status
tree_status_proportions = nyc_trees.status.value_counts()/len(nyc_trees['status'])

