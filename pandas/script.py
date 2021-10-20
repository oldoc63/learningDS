#Exercises:

#Select the description column from reviews and assign the result to the variable desc.

desc = reviews['description']

#Select the first value from the description column of reviews, assigning it to variable first_description.

first_description = reviews.description.iloc[0]

#Select the first row of data (the first record) from reviews, assigning it to the variable first_row.

first_row = reviews.iloc[0]

#Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.

first_descriptions = reviews.description.iloc[:10]

#Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.

indices = [1,2,3,5,8]
sample_reviews = reviews.loc[indices]

#Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100. In other words, generate the following DataFrame:

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

#Create a variable df containing the country and variety columns of the first 100 records. 

cols = ['country', 'variety']
df = reviews.loc[:99, cols]

#Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?

italian_wines = reviews.loc[reviews.country == 'Italy']

#Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.

top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]

