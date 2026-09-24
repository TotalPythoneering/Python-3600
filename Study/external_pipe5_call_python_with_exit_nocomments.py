#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: external_pipe5_call_python_with_exit_nocomments.py
# AUTHOR: Randall Nagy
#
import os
from subprocess import Popen, PIPE

OutFile = "result.tmp"
fout = open(OutFile, "w")

cmd = "python"
if os.name == "posix":
    cmd += "3"

p = Popen([cmd], stdin=PIPE, stdout=fout,
          universal_newlines=True)

for name in ["print('Hello')", "print(5 + 4)", "result = 100 + 20 + 3"]:
    p.stdin.write(name + "\n")
p.stdin.write('exit(result)\n\n')
p.stdin.close();return_code = p.wait();fout.close()

fin = open(OutFile, "r")
zInfo = fin.readlines()
for item in zInfo:
    print("Child:", item.rstrip())
fin.close()

import os
os.remove(OutFile)
print("\n---\nParent: exit(",return_code, ")", sep="")



