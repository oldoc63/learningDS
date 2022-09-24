import numpy as np

# 7 is not included in the range function
die_6 = range(1, 7)
rolls = np.random.choice(die_6, size=2, replace=True)
print(rolls)