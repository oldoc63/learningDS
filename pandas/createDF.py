import pandas as pd

# Create a DataFrame with a dictionary
df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})

#print(df1)

# Create a DataFrame using a list of lists
df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
],
columns=['name', 'address', 'age'])

print(df2)

# Convert a CSV to a DataFrame using .read_csv()
# df = pd.read_csv('pandas/sample.csv')
# print(df)

# Load the CSV below:
# df = pd.read_csv('imdb.csv')
# print(df.head())
# print(df.info())

# Select Columns
customers = pd.DataFrame([
    ["Rebecca Erikson", 35],
    ["Thomas Roberson", 28],
    ["Diane Ochoa", 42]
],
columns= ['name','age'])

print(customers)

customers_name = customers.name

print(customers_name)

customers_age = customers.age

print(customers_age)

# Selecting Multiple Columns

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north_south = df[['clinic_north', 'clinic_south']]

print(type(clinic_north_south))
print(clinic_north_south)

# Select Rows
march = df.iloc[2]
print(march)

# Select Multiple Rows
april_may_june = df.iloc[-3:]
print(april_may_june)

#Select Rows with logic
january = df[df.month == 'January']
print(january)

march_april = df[(df.month == 'March') | (df.month == 'April')]
print(march_april)

january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print(january_february_march)

#Setting indices
df2 = df.loc[[1, 3, 5]]
print(df2)

df3 = df2.reset_index()
print(df3)