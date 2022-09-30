import scipy.stats as stats

# Probability of finding a woman less than 158 cm tall
# stats.norm.cdf(x, loc, scale)
print('Probability of a woman less than 158 cm tall is', stats.norm.cdf(158, 167.64, 8))

# Probability of finding a woman less than 175 cm tall
print('Probability of a woman less than 175 cm tall is', stats.norm.cdf(175, 167.64, 8))

# P(165<X<175) = P(X<175) - P(X<165)
# stats.norm.cdf(x, loc, scale) - stats.norm.cdf(x, loc, scale)
print('Probability of a woman between 165 and 175 cm is', stats.norm.cdf(175, 167.74, 8) - stats.norm.cdf(165, 167.74, 8))

# P(X>172) = 1 - P(X<172)
# 1 - stats.norm.cdf(x, loc, scale)
print('Probability of a woman taller than 172 is', 1 - stats.norm.cdf(172, 167.74, 8))

# Probability of temperature between 18 and 25 degrees Celsius in Galapagos
temp_prob_1 = stats.norm.cdf(25, 20, 3) - stats.norm.cdf(18, 20, 3)
print('Probability of temperature between 18 and 25 degrees Celsius in Galapagos is', temp_prob_1)

# Probability of temperature greater than 24 degrees Celsius in Galapagos
temp_prob_2 = 1 - stats.norm.cdf(24, 20, 3)
print('Probability of temperature greater than 24 degrees Celsius in Galapagos is', temp_prob_2)

import numpy as np

## Exercise 1
# sampling from a 6-sided die
die_6 = range(1, 7)
print(np.random.choice(die_6, size = 5, replace = True))


## Exercise 4 - binomial probability mass function
# 6 heads from 10 fair coin flips
print(stats.binom.pmf(6, 10, 0.5))


## Exercise 6 - binomial probability mass function
# 2 to 4 heads from 10 coin flips
# P(X = 2) + P(X = 3) + P(X = 4)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))

# 0 to 8 heads from 10 coin flips
# 1 - (P(X = 9) + P(X = 10))
print(1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))


## Exercise 9 - binomial cumulative distribution function
# 6 or fewer heads from 10 coin flips
print(stats.binom.cdf(6, 10, 0.5))

# more than 6 heads from 10 coin flips
print(1 - stats.binom.cdf(6, 10, 0.5))

# between 4 and 8 heads from 10 coin flips
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))


## Exercise 10 - normal distribution cumulative distribution function
# stats.norm.cdf(x, loc, scale)
# temperature being less than 14*C
  # x = 14, loc = 20, scale = 3
print(stats.norm.cdf(14, 20, 3))


# Exercise 11
# temperature being greater than 24*C
  # x = 24, loc = 20, scale = 3
print(1 - stats.norm.cdf(24, 20, 3))

# temperature being between 21*C and 25*C
  # x = 24, loc = 20, scale = 3
print(stats.norm.cdf(25, 20, 3) - stats.norm.cdf(21, 20, 3))