import pandas as pd
import matplotlib.pyplot as plt

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