#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-21 11:52:44
# FILE: UdpClientStop.py
# AUTHOR: Randall Nagy
#

# CAVEAT: Do not run BOTH scripts in the IDE.
# Best to run the server script at the CLI.

import socket

server_socket       = ("192.168.1.24", 9000)
max_sz              = 1024

def send(request="stop"):
    msg_buffer = str.encode(request)
    # Creating a UDP Client:
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Sendng a datagram to a UDP Server:
    udp_client.sendto(msg_buffer, server_socket)
    # Get the Server's response:
    response = udp_client.recvfrom(max_sz)
    print(f"Response: [{response}]")

send("Client's Hello!")
#send()
