from scipy.stats import ttest_1samp
import numpy as np

dayly_prices = np.genfromtxt(r'inference\daily_prices.csv', delimiter=',')

