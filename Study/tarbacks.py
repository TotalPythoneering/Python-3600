#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 3600: Inter-
# Process Communications (IPC)''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Project: https://github.com/TotalPythoneering/Python-3600
# DATE: 2021-12-05 06:27:18
# FILE: tarbacks.py
# AUTHOR: Randall Nagy
#
'''
Demonstration Edition: Backup the default folder.
'''
import sys

def tarback(zdays, zpath):
    import os
    import os.path
    import time
    from time import strftime
    from time import gmtime
    zdate = strftime("%Y-%m-%d", gmtime(time.time()))
    zfile = f'./{zdate}_inc{zdays}.tar'
    if not zpath or zdays < 1:
        return False, zfile
    zcmd = f'find {zpath} -type f -mtime -{zdays} | tar -cvf {zfile} -T -'
    print('START:', zcmd)
    print('~*' * 10)
    with os.popen(zcmd, 'r') as proc:
        for ss, line in enumerate(proc, 1):
            print(f'{ss}.)',line, end='')
    print('EXIT', zcmd)
    return True, zfile

zdays = 7
if len(sys.argv) == 2:
    try:
        zdays = int(sys.argv[1])
    except:
        print(f"Usage: {sys.argv[0]} number_of_days")
        
print(f"Find: Backing-up the past {zdays} days.")
response = tarback(zdays, '.')
if response[0] is False:
    print(f'Error: Unable to create {response[1]}')
else:
    print(f'Success: Archive saved to {response[1]} ...')
print(*response)
