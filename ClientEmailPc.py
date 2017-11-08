# Lab 03 Mail Client -- Part Two
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
# Authors: Connor McCauley, Ashley Ottogalli	#
# Email: cmccaul8@uwo.ca, aottogal@uwo.ca 		#
# Date Modified: 2017-11-08						#
# Filename: ClientEmailPc.py					#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #

# ------------------- Additional Information ------------------- #
# Default SMTP Ports: [ 25, 465, 587 ]                           #
# Mail Server: [ 'smtp.gmail.com' ]                              #
# Sender: 'davgren3@gmail.com'                                   #
# Recipient: 'cmccaul8@uwo.ca'                                   #
# -------------------------------------------------------------- #

# BASIC SETUP & INITIALIZATION
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# import statements ::
from socket import *			# import socket module
import base64                   # for encoding auth credentials
import ssl
import smtplib

# define sample message data
msg = "\r\n I love computer networks!"
endmsg = '\r\n.\r\n'  			# msg ends with '.' on a line by itself
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587				    # using default SMTP port

sender = 'davgren3@gmail.com'
subject = 'mail with SMTP'
password = 'theforestthroughttrees'
recipient = 'cmccaul8@uwo.ca'

print("Sending Email")

headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
session = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
session.ehlo()
session.starttls()
session.login(sender, password)
session.sendmail(sender, recipient, headers + "\r\n\r\n" + msg)
session.quit()

