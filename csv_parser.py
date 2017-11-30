import csv

def get_people_from_file(filename):
    people = []
    with open(filename, 'r') as people_file:
        people_matrix = csv.reader(people_file, delimiter=',', quotechar="\"")
        for row in people_matrix:
            people.append((row[0], row[1]))

    return people

def get_exclusions_from_file(filename):
    user_exclusions = []
    with open(filename, 'r') as exclusion_file:
        exclusion_matrix = csv.reader(exclusion_file, \
            delimiter=',', quotechar="\"")
        for row in exclusion_matrix:
            user_exclusions.append((row[0], row[1]))

    return user_exclusions
