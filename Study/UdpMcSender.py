#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-06 18:56:12
# FILE: UdpMcSender.py
# AUTHOR: Randall Nagy
# Mission: Send out SO_BROADCAST messages.
#
import UdpMulticast

UdpMulticast.broadcast("Testing...")
UdpMulticast.broadcast("1...")
UdpMulticast.broadcast("2...")
UdpMulticast.broadcast("3...")
UdpMulticast.broadcast("stop")
