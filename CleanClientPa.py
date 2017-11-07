# Comment Lite (Clean) Version of ClientEmailPa
from socket import *			# import socket module
import base64                   # for encoding auth credentials

msg = "\r\n I love computer networks!"
endmsg = '\r\n.\r\n'
MAIL_PORT = 465

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', MAIL_PORT)

# Create socket called clientSocket and establish a TCP connection with mailserver
# Use SOCK_STREAM for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print("220 reply not received from server.")

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print("250 reply not received from server.")

# Send MAIL FROM command and print server response.
fromCommand = 'MAIL FROM:<deviantverity@gmail.com>\r\n'
clientSocket.send(fromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print("250 reply not received from server.")

# Send RCPT TO command and print server response.
toCommand = 'RCPT TO:<cmccaul8@uwo.ca>\r\n'
clientSocket.send(toCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print("250 reply not received from server.")

# Send DATA command and print server response.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print("354 reply not received from server.")

# Send message data.
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())  # Message ends with a single period.
recvD = clientSocket.recv(1024).decode()
print(recvD)
if recvD[:3] != '250':
    print("250 reply not received from server.")

# Send QUIT command and get server response.
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recvQ = clientSocket.recv(1024).decode()
print(recvQ)
if recvQ[:3] != '221':
    print("221 reply not received from server.")

clientSocket.close()			# close socket when done
