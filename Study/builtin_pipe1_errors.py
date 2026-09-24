#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: builtin_pipe1_errors.py
# AUTHOR: Randall Nagy
#
import os

from subprocess import Popen, PIPE

cmd = ["wait"]    # bash command
if os.name == "nt":
    cmd = ["dir"] # DOS command

try:
    p = Popen(cmd, stdout=PIPE,
              universal_newlines=True) # FileNotFoundError
except Exception as ex:
    print("Error:", ex)

    



