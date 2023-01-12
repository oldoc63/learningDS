import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binom_test

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

# calculate the total number of patients
num_patients = len(heart)
print('Number of patients:', num_patients)

# calculate the number of patients with fbs>120
num_highfbs_patients = np.sum(heart.fbs)
print('Number of patients with fasting blood sugar greater than 120:', num_highfbs_patients)

# calculate 8% of the sample size
print('The 8 percent of the sample size is:', round(0.08*num_patients, 2))

# run binomial test
pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print('The probability of the null hypothesis is:', pval, 'so we can reject it, an accept the alternative')