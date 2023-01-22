import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read in the data
students = pd.read_csv(r'linearRegression\test_data.csv')

print(students.head())

# Write equation for a line
predicted_score = 10 * students.hours_studied + 45

# Create the plot here:
plt.scatter(students.hours_studied, students.score)
plt.plot(students.hours_studied, predicted_score)
plt.show()

# Create the model here:
model = sm.OLS.from_formula('score ~ hours_studied', data=students)

# Fit the model here:
results = model.fit()

# Print the coefficients here:
print(results.params)

# Calculate and print pred_3hr here:
pred_3hr = 9.848 * 3 + 43.016
print(pred_3hr)

# Calculate and print pred_5hr here:
pred_5hr = {'hours_studied':[5]}
print(results.predict(pred_5hr))

# Interpretation of the intercept:
# A student who studied for 0 hours is expected to score 43 on the test.

# Interpretation of the slope:
# For every additional 1 hour of studying, students are expected to score
# 9.8 points higher on the test.

# Calculate `fitted_values` here:
fitted_values = results.predict(students) 

# Calculate `residuals` here:
residuals = students.score - fitted_values

# Print the first 5 residuals here:
print(residuals.head())

# Plot a histogram of the residuals here:
plt.hist(residuals)
plt.show()
plt.clf()

# Plot the residuals against the fitted values here:
plt.scatter(fitted_values, residuals)
plt.show()
plt.clf()

## Create and fit a regression model of score predicted by breakfast
## using sm.OLS.from_formula()

# Calculate and print group means
print(students.groupby('breakfast').mean().score)

# Create the scatter plot of score against breakfast here:
plt.scatter(students.breakfast, students.score)

# Add the additional line using calculated group means
plt.plot([0,1], [61.664151,73.721277])
plt.show()

# Create a regression model of score predicted by breakfast
model = sm.OLS.from_formula('score ~ breakfast', students)

# Fit a regression model of score predicted by breakfast
results = model.fit()

# Print the coefficients
print(results.params)