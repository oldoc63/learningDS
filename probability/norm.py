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