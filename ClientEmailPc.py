# Lab 03 Mail Client -- Part Three
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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# define sample message data
text = "\r\n I love computer networks!"
endmsg = '\r\n.\r\n'  			# msg ends with '.' on a line by itself
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587				    # using default SMTP port

sender = 'davgren3@gmail.com'
subject = 'mail with SMTPLib'
password = 'theforestthroughttrees'
recipient = 'cmccaul8@uwo.ca'
img_path = 'resource/img/kitten.jpg'

print("Sending Email")

msg = MIMEMultipart()
msg["To"] = recipient
msg["From"] = sender
msg["Subject"] = subject

msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (text, img_path), 'html')
msg.attach(msgText)   # Added, and edited the previous line

fp = open(img_path, 'rb')
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(img_path))
msg.attach(img)

session = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
# Send EHLO command using smtplib
session.ehlo()
# Send STARTTLS command using smtplib
session.starttls()
# Send AUTH credentials via login command
session.login(sender, password)
# Send 
session.sendmail(sender, recipient, msg.as_string())
#
session.quit()
# _____________________________________________________________________
exit(code=0)
