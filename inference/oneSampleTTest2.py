from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt(r'inference\daily_prices.csv', delimiter=',')

# day 1
tstat, pval = ttest_1samp(daily_prices[0], 1000)
print('day 1 p-value:', pval)