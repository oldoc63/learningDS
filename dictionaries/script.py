#Creating a dictionary
menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

#TypeError
#powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
#TypeError: unhashable type: 'list'

#Empty Dictionary
empty_dict = {}

#Add A Key
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

menu["cheesecake"] = 8

#Add Multiple Keys
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

sensors.update({"pantry": 22, "guess room": 25, "patio": 34})

print(sensors)

#Overwrite values
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

menu["oatmeal"] = 5

print(menu)

#Dictionary Comprehensions
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}

print(students)

#Get a key
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['water'])

#Get an invalid key
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#print(building_heights['Landmark 81'])
#KeyError: 'Landmark 81'

#To avoid the KeyError first check
key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights['Landmark 81'])

#Try/Except to get a key
key_to_check = "Landmark 81"
try:
    print(building_heights['Landmark 81'])
except KeyError:
    print("That key doesn't exist!")

#Safely Get a Key
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
print(building_heights.get("Shanghai Tower"))

#this line will return None:
print(building_heights.get("My House"))