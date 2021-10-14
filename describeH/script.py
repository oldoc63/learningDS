import pandas as pd 
from matplotlib import pyplot as plt
import codecademylib3_seaborn

cp_data = pd.read_csv("cp.csv") 

plt.hist(cp_data[' Average Covered Charges '], bins=20, edgecolor='black')

plt.title("Distribution of Chest Pain Treatment Cost by Hospital", fontsize = 16)
plt.xlabel("Cost ($)", fontsize = 16)
plt.ylabel("Count", fontsize = 16)

plt.show()
