#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-22 07:25:42
# FILE: SocUdpStopClient.py
# AUTHOR: Randall Nagy
#
import socket

server_socket       = ("127.0.0.1", 9000)
max_sz              = 1024

def send(request="stop"):
    msg_buffer = str.encode(request)
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_client.sendto(msg_buffer, server_socket)
    if request != 'stop':
        response = udp_client.recvfrom(max_sz)
        print(f"Response: [{response}]")
    else:
        print("Shutdown request was sent.")

send("CHello 001!")
send("CHello 002!")
send()
