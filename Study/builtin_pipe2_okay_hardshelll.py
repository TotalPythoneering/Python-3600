#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: builtin_pipe2_okay_hardshelll.py
# AUTHOR: Randall Nagy
#
import os
from subprocess import Popen, PIPE

# POSIX: External command
cmd = ["bash", "-c", "ls", "*.py"]
if os.name == "nt":
    # NT: Internal 'command shell'
    cmd = ["cmd", "/c", "dir", "*.py", "/s"]
    
p = Popen(cmd, stdout=PIPE,
          universal_newlines=True)

for line in p.stdout:
    print(line, end="")
p.stdout.close()
return_code = p.wait()

print("Process terminated with return code: ",
      return_code)


