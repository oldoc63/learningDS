import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Read in the data
codecademy = pd.read_csv('linearRegression/regressCodecademy/codecademy.csv')

# Print the first five rows
print(codecademy.head())

# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed, codecademy.score)

# Show then clear the plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula('score ~ completed', data=codecademy)
results = model.fit()
print(results.params)

# The score is 13.214113 when the prior lessons completed are 0

# The score increase 1.306826 for each lesson completed

# Plot the scatter plot with the line on top
plt.scatter(codecademy.completed, codecademy.score)
plt.plot(codecademy.completed, results.predict(codecademy))
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
prior_20 = {'completed':[20]}
prior_20_score = results.predict(prior_20)
print('The predicted score for a learner who has previosly completed 20 prior lessons is:', prior_20_score)

# Calculated the fitted values for your model and save them as `fitted_values`
fitted_values = results.predict(codecademy)

# Calculate residuals
residuals = codecademy.score - fitted_values

# Check normality assumption by plotting a histogram of the residuals with plt
plt.hist(residuals)
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values, residuals)
plt.show()
plt.clf()

## Do learners who take lesson A or B perform better on the quiz?

# Create a boxplot of score vs lesson
sns.boxplot(x='lesson', y='score', data=codecademy)
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula('score ~ lesson', data=codecademy)
results = model.fit()
print(results.params)

# Calculate and print the group means and mean difference (for comparison)
lessonAMean = np.mean(codecademy.score[codecademy.lesson == 'Lesson A'])
lessonBMean = np.mean(codecademy.score[codecademy.lesson == 'Lesson B'])
differenceAB = lessonAMean - lessonBMean

print('Mean Score [A]:', lessonAMean)
print('Mean Score [B]:', lessonBMean)
print('Mean Score Difference:', differenceAB)

# Or alternatively

print(codecademy.groupby('lesson').mean().score)

# Use sns.lmplot() to plot score vs. completed colored by lesson
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()