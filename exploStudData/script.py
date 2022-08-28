# Load Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
students = pd.read_csv('exploStudData/students.csv')

# Print first few rows of data
print(students.head())

# Print the summary statistics for all columns
print(students.describe())

# Summarize a typical student grade

# Calculate and print the mean value of math_grade with numpy
mean_math_grade = np.mean(students.math_grade)
print(mean_math_grade)

# Calculate and print the mean value of math_grade with pandas
print('mean math_grade', students.math_grade.mean())