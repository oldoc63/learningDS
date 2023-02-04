from matplotlib import pyplot as plt
from script import sales_times1
from script import sales_times2
import numpy as np


# Make a histogram using the list sales_times
plt.hist(sales_times1, bins=20)
plt.show()

# Make two histograms, from two datasets (one much bigger than the other)
# Compare them using density instead of normed (deprecated)
a = np.random.normal(loc=64, scale=2, size=10000)
b = np.random.normal(loc=70, scale=2, size=100000)
 
plt.hist(a, range=(55, 75), bins=20, alpha= 0.5, density=True)
plt.hist(b, range=(55, 75), bins=20, alpha= 0.5, density=True)
plt.show()

# Plot the histogram of sales_times2 on top of sales_times1
plt.hist(sales_times1)
plt.hist(sales_times2)
plt.show()