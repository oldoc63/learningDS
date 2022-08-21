# Initial Data Inspection

import pandas as pd

heart = pd.read_csv('inspectCleanValidate/processed.cleveland.data.csv')
print(heart.head())

print(heart.num.value_counts())

# Data Information
print(heart.info())