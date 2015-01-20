#!/usr/bin/env python3

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import sys
import argparse

#User Options

globalsender = ""
loginrequired = "no"
server = "localhost"
port = "587"
starttls = "no"
username = "username"
password = "password"

#Main Function

def main(to, sender, subject, message, attachment):
	
	msg = MIMEText(message, 'plain')

	if attachment == "html":
		msg = MIMEText(message, 'html')

	if globalsender != "":
		sender = globalsender

	msg['Subject'] = subject
	msg['To'] = to
	msg['From'] = sender
	#msg['Content-Type'] = "text/html; charset='utf-8'"
	#msg['Mime-Version'] = "1.0"
	#msg['Content-Transfer-Encoding'] =  "base64"

	print(msg)

	

	s = smtplib.SMTP(server + ":" + port)

	if starttls == "yes":
		s.starttls()
	if loginrequired == "yes":
		s.login(username, password)
	
	s.send_message(msg)
	s.quit()



if __name__ == "__main()__":
	parser = argparse.ArgumentParser(description='A')

	parser.add_argument('-t', '--to',  dest='users', nargs = '*',
        	           help='Email address of the receiver.')
	parser.add_argument('-s', '--subject', dest = 'subject', nargs = '*',
				help = "Subject of the message")
	parser.add_argument('-m', '--message', dest = 'message', nargs = '*',
				help = "The actual content of the message")
	parser.add_argument('-f', '--sender', dest = 'from', nargs = '*',
        	                help = "Who the message is from")


	args = parser.parse_args()
	to = ", ".join(args.users)
	subject = ' '.join(args.subject)
	message = ' '.join(args.message)

	main(to, sender, subject, message, "plain")

