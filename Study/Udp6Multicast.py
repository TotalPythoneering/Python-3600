#!/usr/bin/env python3
# MISSION: Send, and monitor, SO_BROADCAST messages using IP V6.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-08 16:46:41
# FILE: Udp6Multicast.py
# AUTHOR: Randall Nagy
#
import socket

server_port         = 9000
server_socket       = ("::1", server_port)
max_sz              = 1024

def monitor():
    # Creating a UDP receiver:
    sock = socket.socket(family=socket.AF_INET6, type=socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)   
    # WAS: sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    sock.bind(("", server_port))
    # Monitoring broadcasts:
    while True:
        print("Waiting...")
        request = sock.recvfrom(max_sz)
        print(f"Message: [{request}]")
        if request[0] == b'stop':
            sock.close()
            return

def broadcast(request):
    print(f"Broadcasting [{request}]")
    msg_buffer = str.encode(request)
    # Creating a UDP Client:
    sock = socket.socket(family=socket.AF_INET6, type=socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)   
    # WAS: sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
    # Broadcasting a datagram:
    sock.sendto(msg_buffer, server_socket)
    sock.close()
