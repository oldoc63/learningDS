import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

# load data
heart = pd.read_csv('inference/heartDisease/heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# get cholesterol levels for patients with heart disease
chol_hd = yes_hd.chol

# calculate mean cholesterol levels for patients with heart disease
print(np.mean(chol_hd))

# compare to cut-off for high cholesterol
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

# get cholesterol levels for patients without heart disease
chol_hd = no_hd.chol

# calculate mean cholesterol levels for patients without heart disease
print(np.mean(chol_hd))

# compare to cut-off for high cholesterol
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)