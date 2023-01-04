from scipy.stats import ttest_1samp
import numpy as np

daily_prices = np.genfromtxt(r'inference\daily_prices.csv', delimiter=',')

# day 1
tstat, pval = ttest_1samp(daily_prices[0], 1000)
print('day 1 p-value:', pval)

# 10 days
for i in range(10):
    tstat, pval = ttest_1samp(daily_prices[i], 1000)
    print('day', [i+1], 'the p-value is:', pval)

# Change the Alternative Hypothesis
print('\nDay 1 to 10 with a different alternative hypothesis')
for i in range(10):
    tstat, pval = ttest_1samp(daily_prices[i], 900)
    print('day', [i+1], 'the p-value is:', pval)