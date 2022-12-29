from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

spotify_data = pd.read_csv(r'C:\Users\varic\Documents\learningDS\probability\danceParty\spotify_data.csv')

print(spotify_data.head())