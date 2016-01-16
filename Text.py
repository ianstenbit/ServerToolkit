#!/usr/bin/env python

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendText(text):
		
	
	file = open('config.txt', 'r')

	content = file.read().split('/n')

	sender = content[0]
	password = content[1]
	recipient = content[2]

	#This is a commnent
	servr = smtplib.SMTP("smtp.gmail.com:587")
	servr.starttls()
	servr.login(sender, password)

        
        servr.sendmail(sender, recipient, text.replace('/n/n', '/n'))

	servr.quit()

	print "Sent Text: " + text

