import pandas as pd

#The dictionary-list constructor assigns values to the column labels, but just uses an ascending count from 0 (0, 1, 2, 3, ...) for the row labels. Sometimes this is OK, but oftentimes we will want to assign these labels ourselves.

#The list of row labels used in a DataFrame is known as an Index. We can assign values to it by using an index parameter in our constructor:


pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

#A Series is, in essence, a single column of a DataFrame. So you can assign column values to the Series the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name:


pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

#We'll use the pd.read_csv() function to read the data into a DataFrame.
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv")

#We can use the shape attribute to check how large the resulting DataFrame is:
wine_reviews.shape

#Output
(129971, 14)

#We can examine the contents of the resultant DataFrame using the head() command, which grabs the first five rows:
wine_reviews.head()

#You can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically. To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.
wine_reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

#Exercises:
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

fruit_sales = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index = ['2017 Sales', '2018 Sales'])

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index = ['Fluor', 'Milk', 'Eggs', 'Spam'], name='Dinner')

reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv")

animals.to_csv("cows_and_goats.csv")

#Native Python objects provide good ways of indexing data. Pandas carries all of these over, which helps make it easy to start with.

#In Python, we can access the property of an object by accessing it as an attribute. A book object, for example, might have a title property, which we can access by calling book.title. Columns in a pandas DataFrame work in much the same way.

reviews.country #access the country property of reviews

#If we have a Python dictionary, we can access its values using the indexing ([]) operator. We can do the same with columns in a DataFrame:

reviews['country']

#These are the two ways of selecting a specific Series out of a DataFrame. Neither of them is more or less syntactically valid than the other, but the indexing operator [] does have the advantage that it can handle column names with reserved characters in them (e.g. if we had a country providence column, reviews.country providence wouldn't work).

reviews['country'][0]
out: Italy

#However, pandas has its own accessor operators, loc and iloc. For more advanced operations, these are the ones you're supposed to be using.

#Pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm. To select the first row of data in a DataFrame, we may use the following:

reviews.iloc[0]
out: country                                                    Italy
description    Aromas include tropical fruit, broom, brimston...
                                     ...                        
variety                                              White Blend
winery                                                   Nicosia
Name: 0, Length: 13, dtype: object

#Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, which is column-first, row-second.

#This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns. To get a column with iloc, we can do the following:

reviews.iloc[:, 0]

#On its own, the : operator, which also comes from native Python, means "everything". When combined with other selectors, however, it can be used to indicate a range of values. For example, to select the country column from just the first, second, and third row, we would do:

reviews.iloc[:3, 0]

out:
0       Italy
1    Portugal
2          US
Name: country, dtype: object

#Or, to select just the second and third entries, we would do:

out:
1    Portugal
2          US
Name: country, dtype: object


#It's also possible to pass a list:

reviews.iloc[[0, 1, 2], 0]
out:
0       Italy
1    Portugal
2          US
Name: country, dtype: object

#Finally, it's worth knowing that negative numbers can be used in selection. This will start counting forwards from the end of the values. So for example here are the last five elements of the dataset.

reviews.iloc[-5:]

#The second paradigm for attribute selection is the one followed by the loc operator: label-based selection. In this paradigm, it's the data index value, not its position, which matters.

reviews.loc[0, 'country']

#iloc is conceptually simpler than loc because it ignores the dataset's indices. When we use iloc we treat the dataset like a big matrix (a list of lists), one that we have to index into by position. loc, by contrast, uses the information in the indices to do its work. Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead. For example, here's one operation that's much easier using loc:

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

#the two methods use slightly different indexing schemes.

#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

#Why the change? Remember that loc can index any stdlib type: strings, for example. If we have a DataFrame with index values Apples, ..., Potatoes, ..., and we want to select "all the alphabetical fruit choices between Apples and Potatoes", then it's a lot more convenient to index df.loc['Apples':'Potatoes'] than it is to index something like df.loc['Apples', 'Potatoet'] (t coming after s in the alphabet).

#This is particularly confusing when the DataFrame index is a simple numerical list, e.g. 0,...,1000. In this case df.iloc[0:1000] will return 1000 entries, while df.loc[0:1000] return 1001 of them! To get 1000 elements using loc, you will need to go one lower and ask for df.loc[0:999].

#Label-based selection derives its power from the labels in the index. Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.

#The set_index() method can be used to do the job. Here is what happens when we set_index to the title field:

reviews.set_index('title')

#We often need to ask questions based on conditions. Suppose that we're interested specifically in better-than-average wines produced in Italy. We can start by checking if each wine is Italian or not:

reviews.country == 'Italy'

#Just booleans, wright? Now use it inside loc:

reviews.loc[reviews.country == 'Italy']

#Show all the rows with Italy

#We also wanted to know which ones are better than average. Wines are reviewed on a 80-to-100 point scale, so this could mean wines that accrued at least 90 points. We can use the ampersand (&) to bring the two questions together:

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

#Suppose we'll buy any wine that's made in Italy or which is rated above average. For this we use a pipe (|):


reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]












