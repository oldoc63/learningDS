from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the spotify dataset
spotify_data = pd.read_csv(r'C:\Users\varic\Documents\learningDS\probability\danceParty\spotify_data.csv')

# Preview the dataset
print(spotify_data.head())

# Select the relevant column
song_tempos = spotify_data['tempo'] 

# Plot the population distribution with the mean labeled
population_distribution(song_tempos)

# Sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")

# Sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")

# Sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")

## Calculating Probabilities
population_mean = np.mean(song_tempos)

population_std = np.std(song_tempos)

# Calculate the standard error
standard_error = population_std/(30**.05)

# Calculate the probability of observing an average tempo of 140 bpm or 
# lower from a sample of 30 songs
print(stats.norm.cdf(140, population_mean, standard_error))

# Calculate the probability of observing an average tempo of 150 bpm or 
# higher from a sample of 30 songs
print(1 - stats.norm.cdf(150, population_mean, standard_error))