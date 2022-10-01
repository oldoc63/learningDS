import scipy.stats as stats

# expected value=10, probability of observing 6
print('Probability of raining 6 days Poisson(10) is', stats.poisson.pmf(6, 10))

# Probability of raining 12-14 times Poisson(10)
print('Probability of raining 12-14 times Poisson(10) is', stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10))

# Probability of 15 calls Poisson(15)
print('Probability of 15 calls Poisson(15) is', stats.poisson.pmf(15, 15))