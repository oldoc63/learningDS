import pandas as pd

npi = pd.read_csv('assTwoCatego/npi_sample.csv')

print(npi.head())

# Contingency Tables: crosstab function from pandas
influence_leader_freq = pd.crosstab(npi.influence, npi.leader)
print(influence_leader_freq)

# Investigate association between special and authority
special_authority_freq = pd.crosstab(npi.special, npi.authority)
print(special_authority_freq)

# Contingency Tables: Proportions
influence_leader_prop = influence_leader_freq/len(npi)
print(influence_leader_prop)

# Convert special_authority_freq to proportions
special_authority_prop = special_authority_freq/len(npi)
print(special_authority_prop)