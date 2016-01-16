#!/usr/bin/env python

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "ianlinuxserver@gmail.com"
recipient = "3038153710@mms.att.com"

def sendText(text):

	servr = smtplib.SMTP("smtp.gmail.com:587")
	servr.starttls()
	servr.login(sender, "LinuxMint2015!")

        servr.sendmail(sender, recipient, text)

	servr.quit()

	print "Sent Text: " + text

