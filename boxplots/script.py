import numpy as np
from data import dataset

# Define quartile_one and quartile_three here:
quartile_one = np.quantile(dataset, 0.25)
quartile_three = np.quantile(dataset, 0.75)

#Ignore the code below here
try:
  print("The first quartile of the dataset is " + str(quartile_one) + ".")
except NameError:
  print("You haven't defined quartile_one.")
try:
  print("The third quartile of the dataset is " + str(quartile_three) + ".")
except NameError:
  print("You haven't defined quartile_three.")
