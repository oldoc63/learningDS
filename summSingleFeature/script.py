import pandas as pd

# Import dataset
rentals = pd.read_csv('summSingleFeature/streeteasy.csv')
print(rentals.head())

rentals_subset = rentals[['rent', 'size_sqft', 'borough']]
print(rentals_subset)

# Display summary statistics for all columns
print(rentals_subset.describe(include='all'))