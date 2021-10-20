import pandas as pd

#Pandas comes with a few built-in conditional selectors, two of which we will highlight here.

#The first is isin. isin is lets you select data whose value "is in" a list of values. For example, here's how we can use it to select wines only from Italy or France:

reviews.loc[reviews.country.isin(['Italy', 'France'])]

#The second is isnull (and its companion notnull). These methods let you highlight values which are (or are not) empty (NaN). For example, to filter out wines lacking a price tag in the dataset, here's what we would do:

reviews.loc[reviews.price.notnull()]


