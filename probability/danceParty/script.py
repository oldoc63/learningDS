from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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