#!/usr/bin/python
import smtplib
import itertools
from email.mime.text import MIMEText
from time import localtime, strftime
from pair_randomizer import *
from csv_parser import *
from config import *


# This script will randomly pair two individuals in a given list, less
# a user defined list of pair exceptions, and notify them via email of
# who they should buy a present for (e.g. secret santa).

people = get_people_from_file('people.csv')
valid_pairs = list(itertools.permutations(people.keys(), 2))
user_exclusions = get_exclusions_from_file('exclusions.csv')

for exclusion in user_exclusions:
    valid_pairs.remove(exclusion)
#print("Exclusions: " + str(user_exclusions))
#print("All pairs less exclusions:" + str(valid_pairs))

randomized_senders = generate_random_list(people.keys(), valid_pairs)

print("Final randomized list: " + str(randomized_senders))

# Backup of this year's list for future reference
results_file = open(strftime("%Y-%m-%d", localtime()) + " results.txt", "w")

# Send messages
for pair in randomized_senders:
    giver_email = people[pair[0]]
    msg_body = \
            """{0}: you are {1}'s secret santa.""".format(pair[0],\
                                                          pair[1])

    msg_body = msg_body
    msg = MIMEText(msg_body)
    msg['Subject'] = "Secret Santa"
    msg['From'] = from_email_addr
    msg['To'] = giver_email

    if sending_email:
        mail_server = smtplib.SMTP_SSL(mail_server_url, mail_server_port)
#        mail_server.set_debuglevel(True)
        mail_server.login(mail_server_username, mail_server_password)

        if not testing:
            # send results to all recipients
            mail_server.sendmail(from_email_addr, [giver_email], msg.as_string())

        else:
            # send results to the single testing account
            mail_server.sendmail(from_email_addr, test_email_addr, msg.as_string())

        mail_server.quit()

    else:
            print("(Messages not emailed - check config.py if you would like to change this)")

    # Output results to terminal and backup file.
    print("Notice for {0} sent to {1}".format(pair[0], giver_email))
    results_file.write(pair[0] + " -> " + pair[1] + '\n')

results_file.close()

print('All messages have been sent!')
