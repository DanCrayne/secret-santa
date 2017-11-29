import csv

names = []
emails = []

with open('people.csv', 'r') as people_file:
	people_matrix = csv.reader(people_file, delimiter=',', quotechar="\"")
	for row in people_matrix:
		names.append(row[0])
		emails.append(row[1])

print names
print emails

