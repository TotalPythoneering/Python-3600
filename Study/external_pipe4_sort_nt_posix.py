#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: external_pipe4_sort_nt_posix.py
# AUTHOR: Randall Nagy
#
from subprocess import Popen, PIPE

# A place for the output
OutFile = "result.tmp"
fout = open(OutFile, "w")
# Locate & start the external command
p = Popen(["sort"], stdin=PIPE, stdout=fout,
          universal_newlines=True)
# Write the data to be zInfo
for name in ["Zoe", "Albert", "Todd", "Tes" ]:
    p.stdin.write(name + "\n")
p.stdin.write('\x1a\n') # "Ctrl + Z" / chr(26)
p.stdin.close();return_code = p.wait();fout.close()
# Read what was output
fin = open(OutFile, "r")
zInfo = fin.readlines()
for item in zInfo:
    print(item.rstrip())
fin.close()

import os
# Clean up after ourselves!
os.remove(OutFile)
# Official exit code:
print("\n---\nSort: exit(",return_code, ")", sep="")



