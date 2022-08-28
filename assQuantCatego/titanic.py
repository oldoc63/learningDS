import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv('assQuantCatego/titanic.csv')

print(titanic.head())

# Separate out fares by survival
fares_died = titanic.Fare[titanic.Survived == 0]
fares_survived = titanic.Fare[titanic.Survived == 1]

# Mean difference
mean_fares_died = np.mean(fares_died)
mean_fares_survived = np.mean(fares_survived)
mean_diff = mean_fares_survived - mean_fares_died
print('mean difference: ')
print(mean_diff)

# Median difference
median_fares_died = np.median(fares_died)
median_fares_survived = np.median(fares_survived)
med_diff = median_fares_survived - median_fares_died
print('median difference: ')
print(med_diff)