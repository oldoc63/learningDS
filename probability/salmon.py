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

samp_size = 50

# Generate our random sample below
sample = np.random.choice(np.array(population), samp_size, replace=False)

### Define sample mean below
sample_mean = round(np.mean(sample),3)

### Uncomment the lines below to plot the sample data:
sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()

# loop 500 times to get 500 random sample means
sample_means = []

for i in range(500):
    # take a sample from the data:
    samp = np.random.choice(population, samp_size, replace=False)
    # Calculate the mean of this sample:
    this_sample_mean = np.mean(samp)
    # append this sample mean to a list of sample means
    sample_means.append(this_sample_mean)

# plot all the sample means to show the sampling distribution
sns.histplot(sample_means, stat='density')
plt.title('Sampling distribution of the Mean')
plt.show()