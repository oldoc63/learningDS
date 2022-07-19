print('Hello World'.upper())

print('Hello World'.lower())

print('hello world'.title())

print('Hello World'.split())

print(' '.join(['Hello', 'World']))

print('Hello world'.replace('H', 'J'))

print('   Hello World   '.strip())

print('{} {}'.format('Hello', 'World'))

favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)

#String methods can only create new strings, they do not change the original string
print(favorite_song)

poem_title = 'spring storm'
poem_author = 'William Carlos Williams'

poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author_fixed)
print(poem_author)

#.split() returns a list of substrings found between the given argument
man_its_a_hot_one = 'Like seven inches from the midday sun'
print(man_its_a_hot_one.split())

line_one = 'The sky has given over'
line_one_words = line_one.split()
print(line_one_words)

#The argument for .split() should be provided as a string itself
greatest_guitarist = 'santana'
print(greatest_guitarist.split('n'))
print(greatest_guitarist.split('a'))

#Create a comma separated list of author names
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
print(author_names)