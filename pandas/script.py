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


