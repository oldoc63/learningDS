from song_data import songs
from scipy.stats import iqr

#Create the variables interquartile_range here:
interquartile_range = iqr(songs)

# Ignore the code below here
try:
  print("The IQR of the dataset is " + str(interquartile_range) + "\n")
except NameError:
  print("You haven't defined interquartile_range yet\n")
