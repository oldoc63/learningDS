import scipy.stats as stats

## Probability Mass Function

# expected value=10, probability of observing 6
print('Probability of raining 6 days Poisson(10) is', stats.poisson.pmf(6, 10))

# Probability of raining 12-14 times Poisson(10)
print('Probability of raining 12-14 times Poisson(10) is', stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10))

# Probability of 15 calls Poisson(15)
print('Probability of 15 calls Poisson(15) is', stats.poisson.pmf(15, 15))

# Probability of 7-9 calls Poisson(15)
print('Probability of 7-9 calls Poisson(15) is', stats.poisson.pmf(7, 15) + stats.poisson.pmf(8, 15) + stats.poisson.pmf(9, 15))

## Cumulative Density Function

# Probability of raining 6 or fewer times Poisson(10)
print('Probability of raining 6 or fewer times Poisson(10) is', stats.poisson.cdf(6, 10))

# Probability of raining 12 or more times Poisson(10)
print('Probability of raining 12 or more times Poisson(10) is', 1 - stats.poisson.cdf(11, 10))

# Probability of raining between 12 and 18 times Poisson(10)
print('Probability of raining between 12 and 18 times Poisson(10) is', stats.poisson.cdf(18, 10) - stats.poisson.cdf(11, 10))

# Probability of more than 20 calls Poisson(15)
print('Probability of more than 20 calls Poisson(15) is', 1 - stats.poisson.cdf(20, 10))

# Probability of observing between 17 and 21 calls Poisson(15)
print('Probability of observing between 17 and 21 calls Poisson(15) is', stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15))

## Generate random variable using Poisson Distribution
# stats.poisson.rvs(lamda, size=num_values)
rvs = stats.poisson.rvs(10, size=1000)

import matplotlib.pyplot as plt
import numpy as np

def histogram_function(rand_vars):
  plt.hist(rand_vars, bins = np.arange(len(set(rand_vars)))-0.5, edgecolor = "black")
  plt.xticks(list(range(rand_vars.max())))
  plt.show()

# histogram_function(rvs)

print('The mean of the Poisson generated random variable is', rvs.mean())

# Variance of a Poisson generated random varible using numpy.var()
rand_vars = stats.poisson.rvs(4, size=1000)
print('The variance of the Poisson generated randon variable calculated using numpy.var() is', np.var(rand_vars))

# Take the range of a sample using Python .min() and .max()
print('The range of a random Poisson(4)', min(rand_vars), max(rand_vars))

# Increase lambda to 10 to see the increase in range
rand_vars = stats.poisson.rvs(10, size=1000)
print('The range of a random Poisson(10)', min(rand_vars), max(rand_vars))

# Exercises:

## For checkpoints 1 and 2
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

## Checkpoint 1
# print variance of rand_vars_7
print(np.var(rand_vars_7))

## Checkpoint 2
# print minimum and maximum of rand_vars_7
print(min(rand_vars_7), max(rand_vars_7))


## For checkpoints 3 and 4
# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)

## Checkpoint 3
# print variance of rand_vars_17
print(np.var(rand_vars_17))

# Checkpoint 4
# print minimum and maximum of rand_vars_17
print(min(rand_vars_17), max(rand_vars_17))

# The number of goals a soccer team scores follows Poisson(4).
num_goals = stats.poisson.rvs(4, size=100)
print('The expected num of goals the team will score on 100 games is', num_goals)
print('The variance of num_goals is', np.var(num_goals))

# The team is being robbed. Count each goal as 2 goals.
num_goals_2 = num_goals * 2
print(num_goals_2)

num_goals_2_var = np.var(num_goals) * 2**2
print('The variance of num_goals_2 is', num_goals_2_var)

# How often an emergency team can receive more than 12 calls a day (lambda 9)
calls = 1 - stats.poisson.cdf(12, 9)
print('Probability of observing more than 12 calls', calls)

# Probability of observing a minimum than 10 calls but no more than 12
false_backup = stats.poisson.cdf(12, 9) - stats.poisson.cdf(9, 9)
print('Probability of minimum than 10 calls but no more than 12')