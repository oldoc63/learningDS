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