import pandas as pd

#You can assign either a constant value:

reviews['critic'] = 'everyone'
reviews['critic']

out:

0         everyone
1         everyone
            ...   
129969    everyone
129970    everyone
Name: critic, Length: 129971, dtype: object

#Or with an iterable of values:

reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']

out:

0         129971
1         129970
           ...  
129969         2
129970         1
Name: index_backwards, Length: 129971, dtype: int64


