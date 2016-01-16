#!/usr/bin/env python
import imaplib2
from threading import *
import sys
import email
import re
import Text
import Idler
import time
import subprocess
import os
import SubProcessor

M = None
idler = None
thread = None
process = SubProcessor.SubProcessor(os.getcwd())
Text.sendText("Send password.")

def check():
	#try:
	process_inbox()
	#except:
		#Text.sendText("Error")

def process_inbox():


        #file = open('directory.txt', 'r+')

        #directory = file.read().strip();
        
	rv, data = M.search(None, "(UNSEEN)")
	if rv != 'OK':
		print "No Messages Found!"
		return

	for num in data[0].split():
		rv, data = M.fetch(num, '(RFC822)')
		
		if rv != 'OK':
			print "Error getting message ", num
			return
		
		msg = email.message_from_string(data[0][1])

                msg = msg.as_string()

                msgBody = msg[msg.index('<td>') + 4 : msg.index('</td>')].strip()
		
		M.store(num, '+FLAGS', '\\Deleted')

		response = ""
		if(not process.authorized):
			response = process.authorize("3038153710@mms.att.net", msgBody)
		else:
			response = process.run(msgBody);
		

                if(response.strip() != ""):
                        Text.sendText(response)
                else:
                        Text.sendText(msgBody + " was successfully called.")

	M.expunge()
	print "Leaving Box"

def dosync():
	print "Got an event!"
	check()

def idle():
	needsync = True		
	while True:
			
        	if event.isSet():
           		return
       		 	needsync = False

		def callback(args):
           		 if not event.isSet():
               			 needsync = True
               			 event.set()
	       
        	M.idle(callback=callback)
	   
       		event.wait()
	      
       		if needsync:
           		event.clear()
            		dosync()


M = imaplib2.IMAP4_SSL('imap.gmail.com')
M.login('ianlinuxserver@gmail.com', 'LinuxMint2015!')
M.select("inbox")
check()

#init
thread = Thread(target=idle)
event = Event()

#start
thread.start()

time.sleep(60*60)

#stop
event.set()

#join
thread.join()

M.expunge()
M.close()
M.logout() 
print "DONE!"



