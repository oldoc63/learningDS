# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.hist(flights, range=(0, 365), bins=365, edgecolor="black")
 
plt.title("Frequency of Flights per Year")
plt.xlabel("Days (1 day increments)")
plt.ylabel("Counts")

plt.show()
