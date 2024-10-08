import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

housing = pd.read_csv('assTwoQuant/housing_sample.csv')

# Print the first ten rows of data
print(housing.head(10))

# Plot the area of a rental against its monthly price
plt.scatter(x=housing.price, y=housing.sqfeet) 
plt.xlabel('Rental Price (USD)')
plt.ylabel('Area (Square Feet')
plt.show()

# Plot the area of a rental against the number of bedrooms
plt.scatter(x=housing.beds, y=housing.sqfeet)
plt.xlabel('Number of Bedrooms')
plt.ylabel('Area (Square Feet')
plt.show()

# Calculate the covariance matrix price sqfeet
cov_mat_price_sqfeet = np.cov(housing.price, housing.sqfeet)
print(cov_mat_price_sqfeet)

# Calculate the covariance matrix sqfeet beds
cov_mat_sqfeet_beds = np.cov(housing.sqfeet, housing.beds)
print(cov_mat_sqfeet_beds)

# Save the covariance as a variable named cov_sqfeet_beds
cov_sqfeet_beds = 2.28223306e+02

# pearsonr() function from scipy.stats
from scipy.stats import pearsonr
corr_price_sqfeet, p = pearsonr(housing.price, housing.sqfeet)
print(corr_price_sqfeet)

# Calculate the correlation between sqfeet and beds
corr_sqfeet_beds, p = pearsonr(housing.sqfeet, housing.beds)
print(corr_sqfeet_beds)

# Create sleep dataset from sleep_performance.csv
sleep = pd.read_csv('assTwoQuant/sleep_performance.csv')
print(sleep.head())

# Create a scatter plot with hours_sleep (x axis) and performance (y axis)
plt.scatter(x=sleep.hours_sleep, y=sleep.performance)
plt.xlabel('hours_sleep')
plt.ylabel('performance')
plt.show()

# Calculate the correlation for hours_sleep and performance
corr_sleep_performance, p = pearsonr(sleep.hours_sleep, sleep.performance)
print(corr_sleep_performance)

# Create penguins dataset from penguins.csv
np.set_printoptions(suppress=True, precision=1)

penguins = pd.read_csv('assTwoQuant/penguins.csv')

# Print the first few rows of penguins dataset
print(penguins.head())

# Create scatter plot of flipper_length against body_mass
plt.scatter(x=penguins.flipper_length_mm, y=penguins.body_mass_g)
plt.xlabel('flipper_length_mm')
plt.ylabel('body_mass_g')
plt.show()

# Calculate the covariance matrix flipper_length body_mass
cov_mat_flipper_body = np.cov(penguins.flipper_length_mm, penguins.body_mass_g)
print('Covariance Matrix: ')
print(cov_mat_flipper_body)
print('covariance: ', cov_mat_flipper_body[1][0])

# Calculate the correlation between flipper_lenth and body_mass
corr_flipper_body, p = pearsonr(penguins.flipper_length_mm, penguins.body_mass_g)
print('Correlation: ', corr_flipper_body) 