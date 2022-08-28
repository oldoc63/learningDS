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

# Calculate and print the median of math_grade with pandas
print('median of math_grade: ', students.math_grade.median())

# Calculate and print the mode of math_grade with pandas
print('mode of math_grade: ', students.math_grade.mode()[0])

# Summarize the spread of student grades

# Calculate max and min math_grades
min_math_grade = students.math_grade.min()
print('minimum math grade: ', min_math_grade)

max_math_grade = students.math_grade.max()
print('maximum math_grade: ', max_math_grade)

# Calculate and print the range of the math_grade column
range_math_grade = max_math_grade - min_math_grade
print('The range of the math_grade column is:', range_math_grade)