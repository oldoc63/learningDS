#Open a file and read the whole document
with open('files_in_python/real_cool_document.txt') as cool_doc:
    cool_contents = cool_doc.read()
print(cool_contents)

#Open a file and read it line by line
with open('files_in_python/keats_sonnet.txt') as keats_sonnet:
    for line in keats_sonnet.readlines():
        print(line)

#Reading a Line
with open('files_in_python/millay_sonnet.txt') as sonnet_doc:
    first_line = sonnet_doc.readline()
    second_line = sonnet_doc.readline()
    print(second_line)

#Writing a File
with open('files_in_python/generated_file.txt', 'w') as gen_file:
    gen_file.write("What an incredible file!")

#Appending a File
with open('files_in_python/generated_file.txt', 'a') as gen_file:
    gen_file.write("... and it still is")

#Access files with .close()
fun_cities_file = open('files_in_python/fun_cities_file.txt', 'a')

#We can now append a line to "fun_cities"
fun_cities_file.write("Montréal")

#But we need to remember to close the file
fun_cities_file.close()

#.csv

#Reading a .csv file
import csv

list_of_email_addresses = []
with open('files_in_python/users.csv', newline='') as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_email_addresses.append(row['Email'])

print(list_of_email_addresses)

#Reading different types of CSV files
import csv

with open('files_in_python/addresses.csv', newline='') as addresses_csv:
    address_reader = csv.DictReader(addresses_csv, delimiter=';')
    for row in address_reader:
        print(row['Address'])

#Writing a CSV file
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 

import csv

with open('files_in_python/output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin']
    output_writer = csv.DictWriter(output_csv, fieldnames=fields)
    output_writer.writeheader()
    for item in big_list:
        output_writer.writerow(item)

#Reading a JSON File
import json

with open('files_in_python/purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

print(purchase_data['user'])

#Writing a JSON File
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}

import json

with open('files_in_python/output.json', 'w') as json_file:
    json.dump(turn_to_json, json_file)