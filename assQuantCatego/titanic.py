import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv('assQuantCatego/titanic.csv')

print(titanic.head())

# Separate out fares by survival
fares_died = titanic.Fare['survived' == 0]
fares_surviced = titanic.Fare['survived' == 1]