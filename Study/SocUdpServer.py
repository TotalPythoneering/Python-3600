#!/usr/bin/env python3
# MISSION: Demonstrate the basic socketserver framework opportunities
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-15 05:56:14
# FILE: SocUdpServer.py
# AUTHOR: Randall Nagy
#
import socketserver

server_port         = 9000
server_socket       = ("127.0.0.1", server_port)
max_sz              = 1024

def serve(zHandler):
    server = socketserver.UDPServer(server_socket, zHandler)
    print(f"Monitoring: {type(zHandler)}")
    server.serve_forever()

class MyDatagramHandler(socketserver.DatagramRequestHandler):
    '''
    A BaseRequestHandler uses setup() & finish() to provide self.rfile
    and self.wfile attributes.
    '''
    def setup(self):
        print("SETUP!")
        super().setup()

    def finish(self):
        print("FINISH!")
        super().finish()
        
    def handle(self):
        print(f"Request from: {self.client_address[0]}")
        print(f"Request: {self.rfile.read(max_sz)}")
        print(f"Write: [{self.wfile.write(b'ACK!')}]") 

def monitor():
    serve(MyDatagramHandler)

monitor()

