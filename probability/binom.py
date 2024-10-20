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
print('The probability of 4 to 6 heads from 10 coin flips is', prob_1)

# prob_2 equal to observing more than two heads from 10 coin flips
prob_2 = 1 - (stats.binom.pmf(0, 10, 0.5) + stats.binom.pmf(1, 10, 0.5) + stats.binom.pmf(2, 10, 0.5))
print('The probability of more than two heads from 10 coin flips is', prob_2)

# prob of observing 6 or fewer heads
print('The probability of six or fewer heads is', stats.binom.cdf(6, 10, 0.5))

# prob of observing between 4 and 8 heads
print('The probability between 4 and 8 heads is', stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))

# prob of observing more than 6 heads
print('The probability of observing more than 6 heads is', 1 - stats.binom.cdf(6, 10, 0.5))

# Checkpoint 1
prob_1 = stats.binom.cdf(3, 10, 0.5)
print('Probability of three or fewer heads using cdf', prob_1)

# compare to pmf code
print('Probability of three or fewer heads using pmf', stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))

## Checkpoint 2
prob_2 = 1 - stats.binom.cdf(5, 10, 0.5)
print('Probability of more than five heads is', prob_2)

## probability of observing between two and five heads
prob_3 = stats.binom.cdf(5, 10, 0.5) - stats.binom.cdf(1, 10, 0.5)
print('Probability between two and five heads using cdf is', prob_3)

# compare to pmf code
print('Probability between two and five heads using pmf is', stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))

# A certain basketball player has an 85% chance of making a given free throw and takes 20 free throws
expected_baskets = 20 * 0.85
print('The expected baskets on 20 free throws are', expected_baskets)

variance_baskets = 20 * 0.85 * (1 - 0.85)
print('Variance of free throws made from 20 shots is', variance_baskets)

# Let's say a student has a 98% chance of arriving early or on time to class
expected_late = 180 * (1-0.98)
print('The expected late arrivals are', expected_late)

variance_late = 180 * 0.02 * 0.98
print('Variance of days the student will arrive late is', variance_late)

# At the end of the year, your company's boss decides a bonus of 8% (Average salary $75000)
expected_bonus = 0.08 * 75000
print('The expected end of the year bonus is', expected_bonus)