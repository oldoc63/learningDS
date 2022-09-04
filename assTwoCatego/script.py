import pandas as pd
import numpy as np

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

# Calculate all the marginal proportions from the table influence_leader_prop
leader_marginals = influence_leader_prop.sum(axis=0)
print(leader_marginals)

influence_marginals = influence_leader_prop.sum(axis=1)
print(influence_marginals)

# Calculate all the marginal proportions from the table special_authority_prop
authority_marginals = special_authority_prop.sum(axis=0)
print(authority_marginals)

special_marginals = special_authority_prop.sum(axis=1)
print(special_marginals)

# Use the chi2_contingency() function from SciPy
from scipy.stats import chi2_contingency

chi2, pval, dof, expected = chi2_contingency(influence_leader_freq)
print(np.round(expected))

influence_leader_freq = pd.crosstab(npi.influence, npi.leader)
print(influence_leader_freq)