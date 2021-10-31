import pandas as pd
 
# Load in data
dance_class = pd.read_csv('dance_class_data.csv')
 
# Print the first 10 rows 
print(dance_class.head(10))

'''
Name Gender  Age    Experience
0   Chris Shelton      M   23      beginner
1  Douglas Watson      M   28  intermediate
2    Martha Gomez      F   45      beginner
3      Amos Moore      M   63      beginner
4   Valentina Sen      F   35      beginner
5     Billy Woods      M   53      advanced
6    Oscar Barker      M   43  intermediate
7  Marie Sandoval      F   23      beginner
8   Nancy Mcbride      F   35      beginner
9   Lindsay Bowen      F   27      beginner
'''

print(dance_class.dtypes)

'''
Name          object
Gender        object
Age            int64
Experience    object
'''

#The youngest student in the class is 23 years old and the oldest is 65 years old.

# Store the boundaries
bins = [20, 30, 40, 50, 60, 70]

# Create new binned_age column that bins the values of the ‘Age’ column
dance_class['binned_age'] = pd.cut(dance_class['Age'], bins)

# Print the first few rows of the data
print(dance_class[['binned_age', 'Age']].head())

'''
binned_age  Age
0   (20, 30]   23
1   (20, 30]   28
2   (40, 50]   45
3   (60, 70]   63
4   (30, 40]   35
'''

# Plot the bar graph of binned ages
dance_class['binned_age'].value_counts().plot(kind='bar')
 
# Label the bar graph 
plt.title('Dance Class Age Distribution')
plt.xlabel('Ages')
plt.ylabel('Count') 
 
# Show the bar graph 
plt.show()

#https://www.evernote.com/shard/s468/sh/e0efe392-c19a-4ee0-94d5-c1ce281c7135/a0617eb59f1bb3832b44632d4f3d0ffa

# Store the boundaries
bins = [20, 30, 40, 50, 60, 70]
 
# Store the labels for our bins
age_labels = ['Young Adult', 'Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']
 
# Bin the values of the 'Age' column and specify the labels 
dance_class['binned_age'] = pd.cut(dance_class['Age'], bins, labels = age_labels)

'''
binned_age  Age
0 Young Adult   23
1 Young Adult   28
2 Middle Aged   45
3      Senior   63
4       Adult   35
'''

