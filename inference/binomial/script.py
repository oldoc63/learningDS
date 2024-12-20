import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom_test

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
print('The 95 percent confident limit is:', interval_95)

# report an interval covering 90% of the values of the 500 visitors distribution
null_90CI = np.percentile(null_outcomes, [5, 95])
print('The 90 percent confident limit is:', null_90CI)

# One sided P Value: proportion of 0, 1 or 2 heads in 10000 experiments of 10 coin flips
outcomes = np.array(outcomes)
p_value = np.sum(outcomes <= 2)/len(outcomes)
print('The one-sided p-value for less than or equal 2 heads is:', p_value)

# One sided P value: proportion of values in null_outcomes that are less than or equal to 41
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41.0)/len(null_outcomes)
print('The one-sided p-value for less than or equal 41 purchases is:', p_value)

# Two sided P value: proportion of values in outcomes that are less than or equal 2 or more than or equal 8
outcomes = np.array(outcomes)
p_value = np.sum((outcomes <=2) | (outcomes >= 8)) / len(outcomes)
print('The two-sided p-value for 2 <= heads >=8 is:', p_value)

# Two sided P value: proportion of values in null_outcomes that are 41 <= purchases >= 59
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59)) / len(null_outcomes)
print('The two sided p-value for 41 <= purchases >= 59 is:', p_value)

# Binomial Test Function
def simulation_binomial_test(observed_successes, n, p):
    #initialize null_outcomes
    null_outcomes = []
    #generate the simulated null_distribution
    for i in range(10000):
        simulated_monthly_visitors = np.random.choice(['y','n'], size=n, p=[p, 1-p])
        num_purchased = np.sum(simulated_monthly_visitors == 'y')
        null_outcomes.append(num_purchased)
    #calculate a 1-sided p-value
    null_outcomes = np.array(null_outcomes)
    p_value = np.sum(null_outcomes <= observed_successes) / len(null_outcomes)

    #return the p-value
    return p_value

#Test your function. You should see that your simulation function gives you a 
# very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)

#binom_test() to evaluate if a coin flipped 10 times (trials) and given 
# 2 heads (expected 5) is weighted
p_value = binom_test(2, n=10, p=0.5)
print('Probability of 2 or fewer heads is:', p_value)

#Run binom_test() to see whether the observed 41 purchases among 500 
# visitors to Live-it-LIVE.com is far enough from the expected 10%

print('\nObserved 41 purchases among 500 visitors to Live-it-LIVE.com is far enough from the expected 10%?')

# calculate p_value_2sided here:
p_value_2sided = binom_test(41, 500, 0.1)
print('p_value_2sided:', p_value_2sided)

# calculate p_value_1sided here:
p_value_1sided = binom_test(41, 500, 0.1, alternative='less')
print('p_value_1sided:', p_value_1sided)