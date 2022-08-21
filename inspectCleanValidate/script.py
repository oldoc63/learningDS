# Initial Data Inspection

import pandas as pd

heart = pd.read_csv('inspectCleanValidate/processed.cleveland.data.csv')
print(heart.head())

print(heart.num.value_counts())

# Data Information
print(heart.info())

# Investigate the output at the ca column
print(heart.ca.unique())

# Replace any instance of '?' with np.NaN
import numpy as np

heart['ca'] = heart['ca'].replace({'?': np.nan})

print(heart.ca.unique())

# Investigate the output of the thal column
print(heart.thal.unique())

# Replace any instance of '?' with np.NaN
heart['thal'] = heart['thal'].replace({'?': np.nan})

print(heart['thal'].unique())

# Inspecting Missing Data
print(heart[heart.isnull().any(axis=1)])