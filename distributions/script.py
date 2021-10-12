# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
transactions = pd.read_csv("transactions.csv")

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Use plt.hist() below
plt.hist(cost, range=(0, 165), bins=15,  edgecolor="black")
plt.title("Transactions Cost")
plt.xlabel("Cost in Dollars")
plt.ylabel("Count")

plt.show()
