import pandas as pd

# Import dataset
rentals = pd.read_csv('summSingleFeature/streeteasy.csv')
print(rentals.head())

rentals_subset = rentals[['rent', 'size_sqft', 'borough']]
print(rentals_subset)

# Display summary statistics for all columns
print(rentals_subset.describe(include='all'))

# Import movies dataset and inspect it using .head()
movies = pd.read_csv('summSingleFeature/movies.csv')
print(movies.head())

# Use the .describe() method to display the summary statistics
print(movies.describe(include='all'))

# Calculate the central tendency statistics of rent in rentals_subset

# Mean
rentals_subset.rent.mean()

# Median
rentals_subset.rent.median()

# Mode
rentals_subset.rent.mode()

# Trimmed mean (trim extreme 10%)
from scipy.stats import trim_mean
print(trim_mean(rentals.rent, proportiontocut=0.1))