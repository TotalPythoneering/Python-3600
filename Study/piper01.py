#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 07:38:50
# FILE: piper01.py
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
   os.close(pwrite)
   reader = os.fdopen(pread)
   print(f"{who} reads '{reader.read()}'")   
   sys.exit(0)
else:
   who = "CHILD: "
   os.close(pread)
   writer = os.fdopen(pwrite, 'w')
   message = "HI MOM!"
   print(f"{who} writes '{message}'")
   writer.write(message)
   writer.close()
   sys.exit(0)


