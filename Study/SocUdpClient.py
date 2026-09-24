#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-14 16:42:18
# FILE: SocUdpClient.py
# AUTHOR: Randall Nagy
#
import socket
# MISSION: Demonstrate that clients still work the same!

server_socket       = ("127.0.0.1", 9000)
max_sz              = 1024

def send(request):
    msg_buffer = str.encode(request)
    udp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_client.sendto(msg_buffer, server_socket)
    response = udp_client.recvfrom(max_sz)
    print(f"Response: [{response}]")
    udp_client.close()

send("Client's Hello!")
