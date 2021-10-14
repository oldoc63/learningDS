import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import codecademylib3_seaborn

cp_data = pd.read_csv("cp.csv") 

cp_average = cp_data[' Average Covered Charges '].mean()

cp_median = cp_data[' Average Covered Charges '].median()

plt.hist(cp_data[' Average Covered Charges '], bins=20, edgecolor='black')
plt.hist(cp_data[' Average Total Payments '], bins=20, edgecolor='black')

plt.title("Distribution of Chest Pain Treatment Cost by Hospital", fontsize = 16)
plt.xlabel("Cost ($)", fontsize = 16)
plt.ylabel("Count", fontsize = 16)
plt.axvline(cp_average, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.axvline(cp_median, color='y', linestyle='solid', linewidth=2, label="Median")
plt.legend()

plt.show()
