import scipy.stats as stats

# st.binom.pmf(x, n, p)
#print(stats.binom.pmf(6, 10, 0.5))

# value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)