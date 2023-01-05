import numpy as np
import pandas as pd

monthly_report = pd.read_csv('inference/binomial/monthly_report.csv')

# print the head of monthly_report:
print(monthly_report)

# calculate and print sample_size:
sample_size = len(monthly_report)
print('Sample Size:', sample_size)

#Calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == 'y')
print(num_purchased)