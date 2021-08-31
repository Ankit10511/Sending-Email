#!/usr/bin/env python
# coding: utf-8

# In[2]:


import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    sender_address = 'rtsrivastava4@gmail.com'
    password = getpass.getpass()
    subject = 'AI Mafia - Machine Learning'
    msg = '''
        Hello :)
        I am sending this message to myself
    '''
    # Server initialisation
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, password)

    # Draft message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = 'rtsrivastava4@gmail.com'
    recipients = 'rtsrivastava4@gmail.com'

    server.sendmail(sender_address, recipients, msg.as_string())


send_email()


# In[ ]:




