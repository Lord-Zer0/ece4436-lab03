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
import smtplib

