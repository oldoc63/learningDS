import pandas

commute_df = pandas.read_csv('commute_data.csv')

#print(commute_df.head())

commute_df.columns = ['name', 'total_comm', 'more_than_90', 'state', 'county' ]

print(commute_df.head())