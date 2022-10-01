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
print('Probability of raining 6 or fewer times Poisson(10) is', stats.poisson.cdf(6, 10) )