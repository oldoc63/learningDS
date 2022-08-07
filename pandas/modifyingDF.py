from pyclbr import Function
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
  )

# Adding a column by giving a list of the same length as the existing DataFrame
df['Quantity'] = [100, 150, 50, 35]
print(df)

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

# Add a new column that is the same in all rows
df['In Stock?'] = True
print(df)

# Add a column 'Is taxed?'
df['Is taxed'] = 'Yes'
print(df)

# Add a column by performing a function on the existing columns
df['Sales Tax'] = df.Price * 0.075
print(df)

# Add a column to df called 'Margin'
df['Margin'] = df.Price - df['Cost to Manufacture']
print(df)

# Change the capitalization for name in each row using apply
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Apply the function upper to every row in Name
df['Name'] = df.Name.apply(str.upper)
print(df)

# Apply the function lower to every row in 'Name'.
# Assign these new names to a new column called 'Lowercase Name'.

df['Lowercase Name'] = df.Name.apply(str.lower)
print(df)

# Lambda Function
mylambda = lambda x: (x * 2) + 3
print(mylambda(5))