# need the following to import a file from the parent directory
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("test message body")
msg['Subject'] = "Testing email settings for Secret Santa"
msg['From'] = from_email_addr
msg['To'] = test_email_addr

mail_server = smtplib.SMTP_SSL(mail_server_url, mail_server_port)
mail_server.set_debuglevel(True)
mail_server.login(mail_server_username, mail_server_password)
mail_server.sendmail(from_email_addr, test_email_addr, msg.as_string())
mail_server.quit()
