#!/usr/bin/python

# There is a chance that your email provider will block outgoing messages
# that are not from the same domain as the account from which you are sending.
# (In this case make sure that the "from_email_addr" matches the domain of the
#  user specified by "mail_server_username".)
from_email_addr = "krampus@example.com"
mail_subject = "Secret santa results"

mail_server_url = "smtp.example.com"
mail_server_port = 465
mail_server_username = "user123"
mail_server_password = "password"

# should we send the results to the specified recipients?
sending_email = True

# When in testing mode:
#   1) results will be sent to a single recipient, instead of the addresses
#      in people.csv
testing = True
test_email_addr = "test@example.com"
