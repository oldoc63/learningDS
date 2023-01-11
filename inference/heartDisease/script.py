import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('inference/heartDisease/heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# get cholesterol levels for patients with heart disease
chol_hd = yes_hd.chol