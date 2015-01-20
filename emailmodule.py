#!/usr/bin/env python3

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

import sys
import argparse


def main(to, sender, subject, message, attachment):
	
	msg = MIMEText(message)

	print(msg)
	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = subject
	msg['From'] = "Miro <miro@torma.me>"
	#msg['To'] = to
	msg['To'] = ", ".join(to)
	#msg['To'] = "mirotorma@gmail.com"

	s = smtplib.SMTP('localhost')
	s.send_message(msg)
	s.quit()



if __name__ == "__main()__":
	parser = argparse.ArgumentParser(description='A')
#parser.add_argument('weight', metavar='N', type=int, nargs=1,
 #                  help='an integer for the accumulator')
	parser.add_argument('-t', '--to',  dest='users', nargs = '*',
        	           help='Email address of the receiver.')
	parser.add_argument('-s', '--subject', dest = 'subject', nargs = '*',
				help = "Subject of the message")
	parser.add_argument('-m', '--message', dest = 'message', nargs = '*',
				help = "The actual content of the message")
	parser.add_argument('-f', '--from', dest = 'from', nargs = '*',
        	                help = "Who the message is from")


	args = parser.parse_args()
	to = args.users
	subject = ' '.join(args.subject)
	message = ' '.join(args.message)

	main(to, "", subject, message, "")
#for x in args.subject:
#	string += x



