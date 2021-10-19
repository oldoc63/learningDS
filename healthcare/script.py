import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

print(healthcare.head())
print(healthcare["DRG Definition"].unique())

chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

