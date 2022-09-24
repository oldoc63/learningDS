import numpy as np

# create 6 sided "die"
die_6 = range(1, 7)

# set number of rolls
num_rolls = 10

# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)

results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

