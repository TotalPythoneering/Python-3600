#!/usr/bin/env python3
# MISSION: Demonstrate the TCP/IP connection basics
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2022-06-04 04:51:37
# FILE: TcpStreamCli.py
# AUTHOR: Randall Nagy
#
import TcpStreams

while True:
    print("`q` to quit..")
    request = input("\tSend: ")
    if request == 'q':
        break
    TcpStreams.broadcast(request)

print("\n\nDone!")
