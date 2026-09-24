#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: builtin_pipe3_okay_shell.py
# AUTHOR: Randall Nagy
#
import os
from subprocess import Popen, PIPE

cmd = ["ls", "*.py"]
if os.name == "nt":
    cmd = ["dir", "*.py"] 
p = Popen(cmd, stdout=PIPE,
          shell=True,
          universal_newlines=True)

for line in p.stdout:
    print(line, end="")
    
p.stdout.close()
return_code = p.wait()

print("Process terminated with return code: ",
      return_code)


