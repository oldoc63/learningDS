import numpy as np
from data import dataset

quartile_one = np.quantile(dataset, 0.25) 
quartile_three = np.quantile(dataset, 0.75)

# Define your variables here:
iqr =  quartile_three - quartile_one
distance = 1.5 * iqr
left_whisker = quartile_one - distance
right_whisker = quartile_three + distance

#Ignore the code below here
try:
  print("The interquartile range of the dataset is " + str(iqr) + ".")
except NameError:
  print("You haven't defined iqr.")
  
try:
  print("Each whisker should be " + str(distance) + " units away from the edges of the box.")
except NameError:
  print("You haven't defined distance.")
  
try:
  print("The left whisker should extend to " + str(left_whisker) + " .")
except NameError:
  print("You haven't defined left_whisker.")
  
try:
  print("The right whisker should extend to " + str(right_whisker) + " .")
except NameError:
  print("You haven't defined right_whisker.")
