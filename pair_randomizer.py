import random
"""
 This function tries to generate randomized list. It is not
 deterministic since sometimes excluded (giver,receiver) pairs
 will make generation of a list fail (in this case we return an empty
 list). Running this function until a non-empty list is generated
 could take a few times.
 param people - a complete list of people for which we are generating a
                randomized list for.
                TODO: just extract this list from unique key values in 
                      'valid_pairs'.
 param valid_pairs - a list of valid (giver,receiver) pairs to randomize.
"""
def try_to_generate_random_list(people, valid_pairs):
    already_assigned_to = []
    randomized_senders = []
    for name in people:
        names = [(giver, receiver) for (giver, receiver) in valid_pairs \
                if giver == name and receiver not in already_assigned_to]
        if not names:
            return []

        choice = random.choice(names)
        randomized_senders.append(choice)
        already_assigned_to.append(choice[1])

    return randomized_senders

"""
 This function tries to generate randomized list (see definition of
 'try_to_generate_random_list for details of why it could fail). It
 is possible that this function will either take a very long time to
 return or run an infinite loop if our list of valid pairs is too 
 restrictive (TODO: need to define restrictive).
 param people - a complete list of people for which we are generating a
                randomized list for.
                TODO: just extract this list from unique key values in 
                      'valid_pairs'.
 param valid_pairs - a list of valid (giver,receiver) pairs to randomize.
"""
def generate_random_list(people, valid_pairs):
    # Generate random list until a valid one is found (in some cases,
    # the exclusions will sometimes make list generation fruitless).
    randomized_senders = []
    while randomized_senders == []:
        randomized_senders = try_to_generate_random_list(people, valid_pairs)

    return randomized_senders
