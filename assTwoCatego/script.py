import pandas as pd

npi = pd.read_csv('assTwoCatego/npi_sample.csv')

print(npi.head())

# Contingency Tables: crosstab function from pandas
influence_leader_freq = pd.crosstab(npi.influence, npi.leader)
print(influence_leader_freq)