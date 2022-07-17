import pandas

census_df = pandas.read_csv('census.csv')

#Preview DataFrame
print(census_df.head())

#Rename DataFrame columns
census_df.columns = ['name', 'total_commuters', 'state']