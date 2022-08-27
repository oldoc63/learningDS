import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

students = pd.read_csv('assQuantCatego/students.csv')

# Save scores from each school in two separate lists
scores_GP = students.G3[students.school == 'GP']
scores_MS = students.G3[students.school == 'MS']

# Print the first five rows of students
print(students.head())

# Separate out scores for students who live in urban and rural locations
scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']

# Calculate the means
mean_GP = np.mean(scores_GP)
print(mean_GP)
mean_MS = np.mean(scores_MS)
print(mean_MS)

# Calculate the difference in means G3 score
print(mean_GP - mean_MS)

# Calculate the medians
median_GP = np.median(scores_GP)
print(median_GP)
median_MS = np.median(scores_MS)
print(median_MS)

# Calculate the difference in medians G3 score
print(median_GP - median_MS)

# Same process for scores urban and rural

#calculate means for each group:
scores_urban_mean = np.mean(scores_urban)
scores_rural_mean = np.mean(scores_rural)

#print mean scores:
print('Mean score - students w/ urban address:')
print(scores_urban_mean)
print('Mean score - students w/ rural address:')
print(scores_rural_mean)

#calculate mean difference:
mean_diff = scores_urban_mean - scores_rural_mean

#print mean difference
print('Mean difference:')
print(mean_diff)

#calculate medians for each group:
scores_urban_median = np.median(scores_urban)
scores_rural_median = np.median(scores_rural)

#print median scores
print('Median score - students w/ urban address:')
print(scores_urban_median)
print('Median score - students w/ rural address:')
print(scores_rural_median)

#calculate median difference
median_diff = scores_urban_median - scores_rural_median

#print median difference
print('Median difference:')
print(median_diff)

# Side by Side Box Plots

# Math scores at each school
sns.boxplot(data=students, x='school', y='G3')
plt.show()

# Math scores by address
sns.boxplot(data=students, x='address', y='G3')
plt.show()

# Inspecting Overlapping Histograms

# Investigate association between scores and scholl
plt.hist(scores_GP, color="blue", label="GP", density=True, alpha=0.5)
plt.hist(scores_MS, color="red", label="MS", density=True, alpha=0.5)
plt.legend()
plt.show()

# Investigate association between scores and address
plt.hist(scores_urban, color='blue', label='Urban', density=True, alpha=0.5)
plt.hist(scores_rural, color='red', label='Rural', density=True, alpha=0.5)
plt.legend()
plt.show()