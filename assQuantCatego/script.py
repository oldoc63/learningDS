import numpy as np
import pandas as pd

students = pd.read_csv('assQuantCatego/students.csv')

# Save scores from each school in two separate lists
scores_GP = students.G3[students.school == 'GP']
scores_MS = students.G3[students.school == 'MS']

# Print the first five rows of students
print(students.head())

# Separate out scores for students who live in urban and rural locations
scores_urban = students.G3[students.address == 'U']
scores_rural = students.G3[students.address == 'R']