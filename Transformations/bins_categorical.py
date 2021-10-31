import pandas as pd
 
# read in data
election_data = pd.read_csv('election_data.csv')
 
# get the counts for each candidate
votes = election_data['Vote'].value_counts()
print(votes)

'''
Liliana    1067
John        998
William     494
Emilie      196
Pattie        6
Neil          3
Bob           2
Demi          1
David         1
Hester        1
'''

mask = election_data.isin(votes[votes < 200].index)
election_data[mask] = 'Other'
print(election_data['Vote'].value_counts())

'''
Liliana    1067
John        998
William     494
Other       210
Name: Vote, dtype: int64
'''

