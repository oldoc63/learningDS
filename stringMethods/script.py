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
