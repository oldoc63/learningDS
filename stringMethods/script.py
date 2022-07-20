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

#Create a comma separated list of author's last names
author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])
print(author_last_names)

#Splitting by an escape sequence
smooth_chorus = \
    """And if you said, "This life ain't good enough."
    I would give my world to lift you up
    I could change my life to better suit your mood
    Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)

#Split by lines spring_storm_text
spring_storm_text = \
    """The sky has given over
    its bitterness.
    Out of the dark change
    all day long
    rain falls and falls
    as if it would never end.
    Still the snow keeps
    its hold on the ground.
    But water, water
    from a thousand runnels!
    It collects swiftly,
    dappled with black
    cuts a way for itself
    through green ice in the gutters.
    Drop after drop it falls
    fron the withered grass-stems
    of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

#The string .join() acts on is the delimiter you want to join with
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
print(''.join(my_munequita))

#Join the words in the list to make the first line of the poem
reapers_line_one_word = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_word)
print(reapers_line_one)