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