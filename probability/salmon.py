import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

population = pd.read_csv("probability/salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population), 3)

## Plotting the Population Distribution
sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")

plt.show()
plt.clf() # close this plot

samp_size = 30

# Generate our random sample below
sample = np.random.choice(np.array(population), samp_size, replace=False)