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