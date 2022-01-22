# Importing protocols and modules needed to send a email using python script
import json, smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#Making the message that should be sent
msg = MIMEMultipart()
with open('<Enter your message file here>', 'r') as f:
    message = f.read()
   

#Login into the sender's email address and calling out the subject and the receiver of the email
password = "<Enter your password here>"
msg['From'] = "<Enter Your Email address here>"
msg['To'] = "< Enter the recipient's email here>"
msg['Subject'] = "< Enter your email's subject here>"
msg.attach(MIMEText(message, 'plain'))

#Connecting to the SMTP server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Completing the connection process
server.login(msg['From'], password)

#Adding image attachment
filename = '<enter file name here>'
attachment = open (filename, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

#Sending the email and closing the connection to the SMTP server
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()