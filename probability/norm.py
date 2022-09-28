import scipy.stats as stats

# Probability of finding a woman less than 158 cm tall
# stats.norm.cdf(x, loc, scale)
print('Probability of a woman less than 158 cm tall is', stats.norm.cdf(158, 167.64, 8))