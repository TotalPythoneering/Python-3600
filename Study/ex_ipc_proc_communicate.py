# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: ex_ipc_proc_communicate.py
# AUTHOR: Randall Nagy
# Don't use wait() when you are using multi-PIPE. Use communicate()
#
"""
From the subprocess docs:

    Warning
    Use communicate() rather than .stdin.write, .stdout.read or .stderr.read
    to avoid deadlocks due to any of the other OS pipe buffers filling up and
    blocking the child process.

"""
import subprocess

process = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE,
          stderr=subprocess.PIPE, universal_newlines=True)

out, err = process.communicate()

print(type(out))
print(out)

