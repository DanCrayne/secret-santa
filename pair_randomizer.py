from random import randrange

# code taken from https://www.rosettacode.org/wiki/Knuth_shuffle#Python
def knuth_shuffle(list):
    for i in range(len(list)-1, 0, -1):
        j = randrange(i + 1)
        list[i], list[j] = list[j], list[i]

    return list


'''
 Generates a list of (giver, receiver) pairs, taking into account any
 exclusions (if given).

 param participants - a list of event participants

 param exclusions   - any pairs that are not desired (e.g. couples, etc)
'''

def generate_random_pairs_knuth(participants, exclusions):
    '''
    This algorithm simply randomizes the list of participants and creates
     the pairs by assigning the receiver for each person as the next 
     participant in the list; the final participant is assigned to the first.

     This can be seen as a directed acyclic graph, where each node is a 
     person with exactly one edge entering and another edge leaving it:

     /---------------------\
     \-> a -> b -> c -> d -/

     the pairing result of the above diagram would be [(a,b), (b,c), (c,d), (d,a)]
     Since this list is first randomized, the pairings should be relatively
     unique.

     If there are exclusions, then we walk through the list and make sure
     that the list does not contain an invalid pair. If it does, we 
     re-randomize the list and check again. The exclusions reduce the 
     combinations quite a bit, and could result in an impossible list;
     in this case, the algorithm would never end, and so the script will
     hang. TODO: detect this before trying.
    '''

    done = False

    while not done:
        randomized_participants = knuth_shuffle(participants)

        result = []

        # pair each participant with their proceeding participant
        for i in range(0, len(participants) - 1):
            result.append((randomized_participants[i], randomized_participants[i+1]))

        # pair the last participant with the first
        result.append((randomized_participants[len(participants) - 1], randomized_participants[0]))

        if exclusions:
            # assume list is valid unless proven otherwise
            list_valid = True

            for pair in result:
        
                for exclusion in exclusions:
                    # check if pair names match one of the exclusions
                    # where, each pair has the form:
                    # ((name1, email1), (name2, email2))
                    # and each exclusion has the form (ex_name1, ex_name2)
                    # so we just care about the first element of each participant pair.
                    # (name1, name2) != (ex_name1, ex_name2) and
                    # (name1, name2) != (ex_name2, ex_name1)
                    NAME_ELE = 0
                    if ((   pair[0][NAME_ELE] == exclusion[0]  \
                            and pair[1][NAME_ELE] == exclusion[1]) \
                            or (pair[0][NAME_ELE] == exclusion[1]  \
                            and pair[1][NAME_ELE] == exclusion[0])):
                        list_valid = False

                    if list_valid == False:
                        break

                if list_valid == False:
                    break

        if (list_valid or not exclusions):
            done = True

    return result
