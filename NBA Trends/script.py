import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import seaborn as sns
import matplotlib.pyplot as plt

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

# Save the results as diff_means_2010
diff_means_2010 = knicks_mean_score - nets_mean_score
print(diff_means_2010)

# Create a set of overlapping histograms
plt.title('Histogram of Mets and Knicks Points Scored - 2010')
plt.hist(knicks_pts_10, alpha=0.8, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, label='nets')
plt.legend()
plt.show()

# Filter the values in the DataFrame using the team names and selecting only the pts column
knicks_pts_14 = nba_2014.pts[nba.fran_id=='Knicks']
nets_pts_14 = nba_2014.pts[nba.fran_id=='Nets']

print(knicks_pts_14.head())
print(nets_pts_14.head())

# Use the np.mean() function to calculate the mean points scored for each team.
knicks_mean_score = np.mean(knicks_pts_14) # Mean of Knicks Scores
nets_mean_score = np.mean(nets_pts_14)

print(knicks_mean_score)
print(nets_mean_score)

# Save the results as diff_means_2010
diff_means_2014 = knicks_mean_score - nets_mean_score
print(diff_means_2014)

# Create a set of overlapping histograms
plt.clf()
plt.title('Histogram of Mets and Knicks Points Scored - 2014')
plt.hist(knicks_pts_14, alpha=0.8, label='knicks')
plt.hist(nets_pts_14, alpha=0.8, label='nets')
plt.legend()
plt.show()

# Generate side by side boxplots
plt.clf()
plt.title('Boxplot of Atlantic Division Teams Points Scored - 2010')
sns.boxplot(data=nba_2010, x='fran_id', y='pts')
plt.show()

# Calculate a table of frequencies (games_result and game_location)
location_result_frequency = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print(location_result_frequency)

# Convert this table of frequencies to a table of proportions
location_result_proportions = location_result_frequency/len(nba_2010)
print(location_result_proportions)