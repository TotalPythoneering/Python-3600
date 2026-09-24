# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:05:52
# FILE: callme.py
# AUTHOR: Randall Nagy
#
"""
A simple demonstration
designed to be called from Python
with command-line dirctory arguement(s)
"""
import os, sys

def listdirs(args):
    bag = list()
    for node in args:
        try:
            for file in os.listdir(node):
                dirtest = node + "/" + file
                if os.path.isdir(dirtest):
                    bag.append("Dir: " + dirtest)
                else:
                    bag.append("File: " + node + "/" + file)
        except Exception as ex:
            print("Error:", ex)

    for ref in sorted(bag):
        print(ref.replace("\\","/"))
    return len(bag)

if len(sys.argv) > 1:
    # sys.argv[0] always file name:
    exit(listdirs(sys.argv[1:]))
exit(0)
    
    



