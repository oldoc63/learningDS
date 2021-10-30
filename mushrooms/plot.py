import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

for column in columns:
  #print(column)
  sns.countplot(df[column], order=df[column].value_counts().index)
  plt.title(column + " Value Counts")
  # rotates value labels slightly inc font size
  plt.xticks(rotation=30, fontsize=10)
  # increases variable label font size slightly
  plt.xlabel(column, fontsize=12)
  plt.show()
  plt.clf()










