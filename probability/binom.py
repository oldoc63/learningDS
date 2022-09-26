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

## Question 2
prob_2 = stats.binom.pmf(7, 20, 0.5)
print(prob_2)

# calculating P(2-4 heads) = P(2 heads) + P(3 heads) + p(4 heads) for flipping a coin 10 times
print('The probability of observing between 2 and 4 heads from 10 coin flips is',
 stats.binom.pmf(2, n=10, p=0.5) + stats.binom.pmf(3, n=10, p=0.5) + stats.binom.pmf(4, n=10, p=0.5))

# calculating P(less than 3 heads) = P(0 heads) + P(1 head) +P(2 heads) for flipping a coin 10 times
print('The probability of observing less than 3 heads is', 
stats.binom.pmf(0, 10, 0.5) + stats.binom.pmf(1, 10, 0.5) + stats.binom.pmf(2, 10, 0.5))

# probability of observing 8 or fewer heads
print('The probability of observing 8 or fewer heads',
stats.binom.pmf(0, n=10, p=0.5)
+ stats.binom.pmf(1, n=10, p=0.5)
+ stats.binom.pmf(2, n=10, p=0.5)
+ stats.binom.pmf(3, n=10, p=0.5)
+ stats.binom.pmf(4, n=10, p=0.5)
+ stats.binom.pmf(5, n=10, p=0.5)
+ stats.binom.pmf(6, n=10, p=0.5)
+ stats.binom.pmf(7, n=10, p=0.5)
+ stats.binom.pmf(8, n=10, p=0.5))

# probability of less than or equal to 8
print('The probability of less than or equal to 8 is', 
1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))

# prob_1 equal to the probability of observing between 4 to 6 heads from 10 coin flips
prob_1 = stats.binom.pmf(4, 10, 0.5) + stats.binom.pmf(5, 10, 0.5) + stats.binom.pmf(6, 10, 0.5)
print(prob_1)