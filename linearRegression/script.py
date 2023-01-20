import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv(r'linearRegression\test_data.csv')

print(students.head())

# Write equation for a line
predicted_score = 10 * students.hours_studied + 45

# Create the plot here:
plt.scatter(students.hours_studied, students.score)
plt.plot(students.hours_studied, predicted_score)
plt.show()