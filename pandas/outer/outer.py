import pandas as pd

company_a = pd.DataFrame([
    ['Sally Sparrow', 'sally.sparrow@gmail.com'],
    ['Peter Grant', 'pgrant@yahoo.com'],
    ['Leslie May', 'leslie_may@gmail.com']
    ],
    columns=['name','email']
)

company_b = pd.DataFrame([
    {'name': 'Peter Grant','phone': '212-345-6789'},
    {'name': 'Leslie May', 'phone': '626-987-6543'},
    {'name': 'Aaron Burr', 'phone': '303-456-7891'}
])

print(company_a)

print(company_b)

# Outer Join
outer_merge = pd.merge(company_a, company_b, how='outer')

print(outer_merge)

# Big Super Store
store_a = pd.read_csv('pandas/outer/store_a.csv')
print(store_a)

store_b = pd.read_csv('pandas/outer/store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(store_a, store_b, how='outer')
print(store_a_b_outer)