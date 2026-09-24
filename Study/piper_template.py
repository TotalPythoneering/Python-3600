#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 07:40:32
# FILE: piper_template.py
# AUTHOR: Randall Nagy
#
"""
POSIX: Forking children that use file handles.
NOTE:  *** WILL NOT WORK ON Microsoft WINDOWS ***
"""
import os
import sys

who = None
pread, pwrite = os.pipe()
proc_id = os.fork() # POSIX, only.
if proc_id:
   who = "PAREN: "
   # TODO: Parent Logic
else:
   who = "CHILD: "
   # TODO: Child Logic


