import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import seaborn as sns

np.set_printoptions(suppress=True, precision=2)

nba = pd.read_csv('NBA Trends/nba_games.csv')

# print(nba.head)

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

# print(nba_2010.head())

# Filter the values in the DataFrame using the team names and selecting only the pts column
knicks_pts_10 = nba_2010.pts[nba.fran_id=='Knicks']
nets_pts_10 = nba_2010.pts[nba.fran_id=='Nets']

print(knicks_pts_10.head())
print(nets_pts_10.head())

# Use the np.mean() function to calculate the mean points scored for each team.
knicks_mean_score = np.mean(knicks_pts_10) # Mean of Knicks Scores
nets_mean_score = np.mean(nets_pts_10)

print(knicks_mean_score)
print(nets_mean_score)