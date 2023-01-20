import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv(r'linearRegression\test_data.csv')

print(students.head())

# Write equation for a line
y = 9.85 * students.hours_studied + 43

# Create the plot here:
plt.scatter(students.hours_studied, students.score)
plt.xlabel('Hours Studied')
plt.ylabel('Score')

plt.plot(students.hours_studied, y)
plt.show()