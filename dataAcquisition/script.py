import csv

with open('census.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(r.json())