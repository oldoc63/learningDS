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

