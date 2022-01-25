"""
This small snippet actually just reads the log file in its entirety.

"""

logfile="access.log"

with open(logfile) as f:
    log = f.read()
    print(log)