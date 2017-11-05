# Lab 03 Skeleton Code for Mail Client
# import socket module
from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
MAIL_PORT = 25  # using default SMTP port
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmx.com", MAIL_PORT)
# Create socket called clientSocket and establish a TCP connection with mailserver
# Use SOCK_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print("Message Received" + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send MAIL FROM command and print server response.
# Fill in start
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
# Fill in end
# Send DATA command and print server response.
# Fill in start
# Fill in end
# Send message data.
# Fill in start
# Fill in end
# Message ends with a single period.