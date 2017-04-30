#!/usr/bin/env python

import smtplib


def sendText(text, sender, password, recipient):
    servr = smtplib.SMTP("smtp.gmail.com:587")
    servr.starttls()
    servr.login(sender, password)

    servr.sendmail(sender, recipient, text.replace('/n/n', '/n'))

    servr.quit()

    print "Sent Text: " + text
