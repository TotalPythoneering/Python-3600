#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-08 16:28:05
# FILE: Udp6McSender.py
# AUTHOR: Randall Nagy
# Mission: Send out SO_BROADCAST messages.
#
import Udp6Multicast

Udp6Multicast.broadcast("Testing...")
Udp6Multicast.broadcast("1...")
Udp6Multicast.broadcast("2...")
Udp6Multicast.broadcast("3...")
Udp6Multicast.broadcast("stop")
