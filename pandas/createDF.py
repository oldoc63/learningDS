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
df = pd.read_csv('pandas/sample.csv')
print(df)

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