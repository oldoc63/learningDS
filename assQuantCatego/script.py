import numpy as np
import pandas as pd

students = pd.read_csv('assQuantCatego/students.csv')

# Save scores from each school in two separate lists
scores_GP = students.G3[students.school == 'GP']
scores_MS = students.G3[students.school == 'MS']