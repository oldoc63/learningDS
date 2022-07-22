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

#Join the words in the list with a space to make the first line of the poem
reapers_line_one_word = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_word)
print(reapers_line_one)

#Join the words in the list with a comma
santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)

#Join using escape sequences as the delimiter
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']
smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
print(smooth_fifth_verse)

#Join winter_trees_lines with the escape '\n'
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

#Python provides a great method for cleaning strings: .strip()
featuring = "          rob thomas         "
print(featuring.strip())

#.strip() with a character argument, will strip that character
featuring = '!!!rob thomas       !!!'
print(featuring.strip('!'))

#love_maybe lines stripped
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []

for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

#Replace takes two arguments and replaces all instances of the first argument with the second.
#string_name.replace(substring_being_replaced, new_substring)
with_spaces = 'You got the kind of loving that can be so smooth'
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)

#toomer_bio_fixed
toomer_bio = \
    """
    Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
    """
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

#.find(): takes a string as an argument and search the string it was running on for that string
print('smooth'.find('t'))

#.find() can search for larger strings and return the index value of the first character
print('smooth'.find('oo'))

#Find 'disown' in the first line of Gabriela Mistral's poem
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

#.format() is a handy method for including variables in strings
# def favorite_song_statement(song, artist):
#     return "My favorite song is {} by {}.".format(song, artist)

# print(favorite_song_statement('Smooth', 'Santana'))
# => "My favorite song is Smooth by Santana."

#Write a function called poem_title_card
def poem_title_card(title, poet):
    poem_desc = "The poem \"{}\" is writen by {}.".format(title, poet)
    return poem_desc

print(poem_title_card("I Hear America Singing", "Walt Whitman"))

#Including keywords in the string and the arguments to remove ambiguity
# def favorite_song_statement(song, artist):
#     return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

# print(favorite_song_statement('Maria, Maria', 'Santana'))

def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)

print(favorite_song_statement('Smooth', 'Santana'))
# => "My favorite song is Smooth by Santana."

# Fix function poem_description by using keywords
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein", title = "My Beard", original_work = "Where the Sidewalk Ends", publishing_date = "1974")

print(my_beard_description)

#Preserve the Verse final task
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

#Split highlighted_poems at the commas
highlighted_poems_list = highlighted_poems.split(',')