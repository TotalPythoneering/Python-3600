# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: ex_sys_path.py
# AUTHOR: Randall Nagy
#
import sys

# Quick path check
print("sys:", *enumerate(sys.path))

print("\n\n")

# Nicer path report
for ss, node in enumerate(sys.path):
    print(ss+1, "=", node)
    



