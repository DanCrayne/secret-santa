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

participants = get_people_from_file('people.csv')
exclusions = get_exclusions_from_file('exclusions.csv')
randomized_senders = generate_random_pairs_knuth(participants, exclusions)

#print("Final randomized list: " + str(randomized_senders))

# Backup of this year's list for future reference
results_file = open(strftime("%Y-%m-%d", localtime()) + " results.txt", "w")

if sending_email:
    mail_server = smtplib.SMTP_SSL(mail_server_url, mail_server_port)
#    mail_server.set_debuglevel(True)
    mail_server.login(mail_server_username, mail_server_password)

for pair in randomized_senders:
    giver_email = pair[0][1]
    msg_body = \
            """{0}: you are {1}'s secret santa.""".format(pair[0][0],\
                                                          pair[1][0])

    msg_body = msg_body
    msg = MIMEText(msg_body)
    msg['Subject'] = mail_subject
    msg['From'] = from_email_addr
    msg['To'] = giver_email

    if sending_email:
        if not testing:
            # send results to all recipients
            mail_server.sendmail(from_email_addr, giver_email, msg.as_string())
            print("Notice for {0} sent to {1}".format(pair[0][0], pair[0][1]))

        else:
            # send results to the single testing account
            mail_server.sendmail(from_email_addr, test_email_addr, msg.as_string())
            print("Notice for {0} sent to {1}".format(pair[0][0], test_email_addr))

    else:
        print("Generated gift recipient for {0}".format(pair[0][0]))


    # Output results to terminal and backup file.
    results_file.write(pair[0][0] + " -> " + pair[1][0] + '\n')

if sending_email:
    mail_server.quit()

results_file.close()

if sending_email:
    print('All messages have been sent!')
else:
    print("Messages not emailed - check config.py if you would like to change this")
