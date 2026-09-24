#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:54
# FILE: MyStderr02.py
# AUTHOR: Randall Nagy
# File: MyStderr02.py
#
import MySms as sms # Case Sensitive!
import sys

name = input("Enter Name:")
try:
    number = int(input("Enter Number:"))
except ValueError as ex:
    print(ex, file=sys.stderr, flush=True)
    send = sms.SmptServer()
    send.sendSMS("TC002 Failure")
    sys.exit(-1) # OS Return Code!

print("Success:", name, number)
sys.exit(1)


