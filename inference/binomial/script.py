import numpy as np
import pandas as pd

monthly_report = pd.read_csv('inference/binomial/monthly_report.csv')

# print the head of monthly_report:
print(monthly_report)

# calculate and print sample_size:
sample_size = len(monthly_report)
print('Sample Size:', sample_size)

# calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == 'y')
print(num_purchased)

# simulate one visitor:
one_visitor = np.random.choice(['y','n'], size=1, p=[0.1,0.9])
print(one_visitor)

# simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y','n'], size=500, p=[0.1,0.9])
print(simulated_monthly_visitors)

# simulate 10 coin flips and print out the number of heads
flips = np.random.choice(['heads', 'tails'], size=10, p=[0.5,0.5])
number_heads = np.sum(flips == 'heads')
print(number_heads)