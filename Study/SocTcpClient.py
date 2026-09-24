#!/usr/bin/env python3
# MISSION: Demonstrate the TCP/IP connection basics
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-14 15:22:06
# FILE: SocTcpClient.py
# AUTHOR: Randall Nagy
#
import socket

server_port         = 9000
server_socket       = ("127.0.0.1", server_port)
max_sz              = 1024

def broadcast(request):
    print(f"Broadcasting [{request}]")
    msg_buffer = str.encode(request)
    # Creating a TCP/IP Client:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_socket)
        sock.sendall(msg_buffer)
        data = sock.recv(max_sz)
        print(f'Received [{data}]')

broadcast("Yello!")
