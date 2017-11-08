# Lab 03 Mail Client -- Part One
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= #
# Authors: Connor McCauley, Ashley Ottogalli	#
# Email: cmccaul8@uwo.ca, aottogal@uwo.ca 		#
# Date Modified: 2017-11-06						#
# Filename: ClientEmailPa.py					#
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

# define sample message data
msg = "\r\n I love computer networks!"
endmsg = '\r\n.\r\n'  			# msg ends with '.' on a line by itself
MAIL_PORT = 587				    # using default SMTP port

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', MAIL_PORT)

# Create socket called clientSocket and establish a TCP connection with mailserver
# Use SOCK_STREAM for TCP ------------------------------	
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# server response | expected code: 220 -----------------
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':			# reply err: expected reply not received
    print("220 reply not received from server.")

# Send HELO command and print server response.
# =====================================================================
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
# server response | expected code: 250 -----------------
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':			# reply err: expected reply not received
    print("250 reply not received from server.")

# =====================================================================
# Secure Authentication Layer (TLS/SSL Commands Follow)
# =====================================================================
# Send STARTTLS command and print server response.
stlsCommand = 'STARTTLS\r\n'
clientSocket.send(stlsCommand.encode())
# server response | expected code: 220 -----------------
recvtls = clientSocket.recv(1024).decode()
print(recvtls)
if recvtls[:3] != '220':			# reply err: expected reply not received
    print("220 reply not received from server.")

# Send AUTH command and print server response.
authCommand = 'AUTH LOGIN\r\n'
clientSocket.send(base64.b64encode('\x00' + authCommand))
# server response | expected code: 220 -----------------
recva1 = base64.b64decode(clientSocket.recv(1024))
print(recva1)
if recva1[:3] != '220':			# reply err: expected reply not received
    print("220 reply not received from server.")

# Send base64 encrypted username
username = "davgren3"
user64 = base64.b64encode(('\x00' + username).encode('utf-8'))     # encrypt username
clientSocket.send(user64)
# server response | expected code: 250 -----------------
recva2 = clientSocket.recv(1024).decode()
print(recva2)

# Send base64 encrypted password
password = 'theforestthroughttrees'
pass64 = base64.b64encode(('\x00' + password).encode('utf-8'))     # encrypt password
clientSocket.send(pass64)
# server response | expected code: 250 -----------------
recva3 = clientSocket.recv(1024).decode()
print(recva3)

# ... more stuff goes here ...

# Send MAIL FROM command and print server response.
# =====================================================================
fromCommand = 'MAIL FROM:<davgren@gmail.com>\r\n'
clientSocket.send(fromCommand.encode())
# server response | expected code: 250 -----------------
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':			# reply err: expected reply not received
    print("250 reply not received from server.")

# Send RCPT TO command and print server response.
# =====================================================================
toCommand = 'RCPT TO:<cmccaul8@uwo.ca>\r\n'
clientSocket.send(toCommand.encode())
# server response | expected code: 250 -----------------
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':			# reply err: expected reply not received
    print("250 reply not received from server.")

# Send DATA command and print server response.
# =====================================================================
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
# server response | expected code: 354 -----------------
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':			# reply err: expected reply not received
    print("354 reply not received from server.")

# Send message data.
# =====================================================================
clientSocket.send(msg.encode())
# end of message
clientSocket.send(endmsg.encode())	# Message ends with a single period.
recvD = clientSocket.recv(1024).decode()
# server response | expected code: 250 -----------------
print(recvD)
if recvD[:3] != '250':			# reply err: expected reply not received
    print("250 reply not received from server.")

# Send QUIT command and get server response.
# =====================================================================
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
# server response | expected code: 221 -----------------
recvQ = clientSocket.recv(1024).decode()
print(recvQ)
if recvQ[:3] != '221':			# reply err: expected reply not received
    print("221 reply not received from server.")

# _____________________________________________________________________

clientSocket.close()			# close socket when done
