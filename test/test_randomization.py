# need the following to import a file from the parent directory
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from csv_parser import *
from pair_randomizer import *

participants = get_people_from_file('../people.csv')
exclusions = get_exclusions_from_file('../exclusions.csv')

print("participants:", participants)
print("exclusions:", exclusions)

participants_list = []
exclusions_list = []

for key in participants:
    participants_list.append((key, participants[key]))

#for key in exclusions:
#    exclusions_list.append((key, exclusions[key]))

#print("participants: ", participants_list)
#print("exclusions: ", exclusions)

randomized_pairs = generate_random_pairs_knuth(participants_list, exclusions)

for pair in randomized_pairs:
    print(pair)
#print(randomized_pairs)
