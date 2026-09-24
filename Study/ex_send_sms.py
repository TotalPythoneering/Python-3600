# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: ex_send_sms.py
# AUTHOR: Randall Nagy
# File: ex_send_sms.py
#

import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('EmailNoj@gmail.com', 'EmailNoj9000')

# SMS Gateway list:
# https://en.wikipedia.org/wiki/SMS_gateway
FakePhone = '1234567890'
server.sendmail(
    'EmailNoj@gmail.com',
    FakePhone + '@mms.att.net',
    'Greetings!')
