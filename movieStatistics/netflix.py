import pandas as pd
import numpy as np

# Language variable on films

# Dictionary
langDic = { 'language':['english', 'spanish', 'hindi', 'french', 'otherSingle', 'multiple'],
            'frequency': [360, 29, 27, 15, 51, 21]
}

# Convert a dictionary to a DataFrame
df1 = pd.DataFrame(langDic, columns = ['language', 'frequency'])
print(df1)
print(type(df1))

# Calculating Percentage
df1['percent'] = (df1['frequency'] / df1['frequency'].sum()) * 100

# Show the dataframe
print(df1)

def ratioFunction():
   num1 = input('Enter the first number: ')
   num1 = int(num1) # Now we are good
   num2 = input('Enter the second number: ')
   num2 = int(num2) # Good, good
   ratio12 = float(num1/num2)
   print('The ratio of', num1, 'and', num2,'is', str(ratio12) + '.')

ratioFunction()
