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

# Calculate the central tendency statistics of movies dataset

# Save the mean to mean_budget
mean_budget = movies.production_budget.mean()
print(mean_budget)

# Save the median to med_budget
med_budget = movies.production_budget.median()
print(med_budget)

# Save the mode to mode_budget
mode_budget = movies.production_budget.mode()

# Save the trimmed mean to trmean_budget
trmean_budget = trim_mean(movies.production_budget, proportiontocut=0.2)
print(trmean_budget)

# Spread for quantitative data for rentals dataset

# Range
rentals.rent.max() - rentals.rent.min()

# Interquartile Range
rentals.rent.quantile(0.75) - rentals.rent.quantile(0.25)

from scipy.stats import iqr
iqr(rentals.rent) #alternative way

# Variance
rentals.rent.var()

# Standard deviation
rentals.rent.std()

#Mean absolute deviation
rentals.rent.mad()

# Spread for quantitiative data for movies dataset

# Save the range to range budget
range_budget = movies.production_budget.max() - movies.production_budget.min()
print(range_budget)

# Save the interquartile budget to iqr_budget
iqr_budget = movies.production_budget.quantile(.75) - movies.production_budget.quantile(.25)
print(iqr_budget)

# Save the variance to var_budget
var_budget = movies.production_budget.var()
print(var_budget)

# Save the standard deviation to std_budget
std_budget = movies.production_budget.std()
print(std_budget)

# Save the mean absolute deviation to mad_budget
mad_budget = movies.production_budget.mad()
print(mad_budget)

# Visualizing Quantitative Variables

import matplotlib.pyplot as plt
import seaborn as sns

# Boxplot for rent
sns.boxplot(x='rent', data=rentals)
plt.show()
plt.close()

# Histogram for rent
sns.histplot(x='rent', data=rentals)
plt.show()
plt.close()

# Create a boxplot for movie budget
sns.boxplot(x='production_budget', data=movies)
plt.show()
plt.close()

# Create a histplot for movie budget
sns.histplot(x='production_budget', data=movies)
plt.show()
plt.close()

# Value Counts for Categorical Data

# Counts of rental listings in each borough
print(rentals.borough.value_counts())

# Save the counts to genre counts
genre_counts = movies.genre.value_counts()
print(genre_counts)