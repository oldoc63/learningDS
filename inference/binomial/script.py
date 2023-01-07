import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# simulate 500 monthly visitors who purchased
num_purchased = np.sum(simulated_monthly_visitors == 'y')
print(num_purchased)

# initialize an empty list named outcomes to store the number of heads
outcomes = []
# set up a for loop to repeat the steps below 10000 times
for i in range(10000):
    # flip a fair coin 10 times
    flips = np.random.choice(['heads', 'tails'], size=10, p=[0.5,0.5])
    # calculate the number of those 10 flips that came up heads
    num_heads = np.sum(flips == 'heads')
    # append num_heads onto outcomes
    outcomes.append(num_heads)
print(outcomes)

min_heads = np.min(outcomes)
print(min_heads)

max_heads = np.max(outcomes)
print(max_heads)

# randomly sample 500 visitors who each have a 10% chance of making a purchase
null_outcomes = []
for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)
print(null_outcomes)

# calculate the minimum and maximum values in null outcomes here:
null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)
print(null_min, null_max)

# inspect the distribution of the number of heads with matplotlib.pyplot.hist()
plt.hist(outcomes)
plt.axvline(2, color='r')
plt.show()

# inspect the distribution of randomly sampling 500 visitors with 10% chance of making a purchase using matplotlib.pyplot.hist()
plt.hist(null_outcomes)
# add a vertical line to your histogram at 41
plt.axvline(41, color='r')
plt.show()

# report an interval covering 95% of the values of the 500 visitors distribution
interval_95 = np.percentile(null_outcomes, [2.5, 97.5])
print(interval_95)

# report an interval covering 90% of the values of the 500 visitors distribution
null_90CI = np.percentile(null_outcomes, [5, 95])
print(null_90CI)