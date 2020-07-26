# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:09:29 2020

@author: coder_ritvik
"""
import smtplib #secured mail transfer protocol library 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
email_user="ritvikmahajan99@gmail.com"
email_send="manishagupta0077@gmail.com"
subject="pyhton"
body="hello mom"
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
msg['Subject']=subject
msg.attach(MIMEText(body,'plain'))
text=msg.as_string()


server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls() #transport layer securuty

server.login(email_user,"ritshika")


server.sendmail(email_user,email_send,text)
server.quit()