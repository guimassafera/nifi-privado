# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()

message = "xalalalaaaaaaaaaaaa"

# setup the parameters of the message
password = "#GFm06051993@"
msg['From'] = "guilhermefmassafera@gmail.com"
msg['To'] = "guilherme.massafera@shipay.com.br"
msg['Subject'] = "Descrição"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print
"successfully sent email to %s:" % (msg['To'])
