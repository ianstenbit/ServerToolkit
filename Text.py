#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendText(text, sender, password, recipient):

	#This is a commnent
	servr = smtplib.SMTP("smtp.gmail.com:587")
	servr.starttls()
	servr.login(sender, password)

        
        servr.sendmail(sender, recipient, text.replace('/n/n', '/n'))

	servr.quit()

	print "Sent Text: " + text

