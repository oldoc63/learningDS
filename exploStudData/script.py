# Load Libraries
from locale import normalize
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

# Calculate and print the standard deviation of the math_grade
std_math_grade = students.math_grade.std()
print('The standard deviation of the math_grade is:', std_math_grade)

# Calculate the mean absolute deviation of the math_grade
mad_math_grade = students.math_grade.mad()
print('The mean absolute deviation of the math_grade is:', mad_math_grade)

# Visualize the distribution of student grades

# Create a histogram of math grades
sns.histplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Create a box plot of math grades
sns.boxplot(x='math_grade', data=students)
plt.show()
plt.clf()

# Calculate number of students with mothers in each job category
print(students.Mjob.value_counts())

# Calculate proportion of students with mothers in each job category
print(students.Mjob.value_counts(normalize=True))

# Create bar chart of Mjob
sns.countplot(x='Mjob', data=students)
plt.show()
plt.clf()

# Create pie chart of Mjob
students.Mjob.value_counts().plot.pie()
plt.show()