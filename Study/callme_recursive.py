# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: callme_recursive.py
# AUTHOR: Randall Nagy
#
"""
A simple demonstration
designed to be called from Python
with command-line directory arguement(s)
"""
import os, sys

def listdirs(args):
    total = 0
    for node in args:
        print("Directory of: {}".format(node))
        try:
            for file in os.listdir(node):
                dirtest = node + "/" + file
                if os.path.isdir(dirtest):
                    # Directory recursion
                    total += listdirs([dirtest])
                else:
                    total += 1
        except FileNotFoundError as ex:
            print("\tError:", ex)
        except PermissionError:
            pass       
    return total


if len(sys.argv) > 1:
    exit(listdirs(sys.argv[1:]))
exit(0)
    
    



