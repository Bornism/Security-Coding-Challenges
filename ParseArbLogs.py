"""
This code will specifically look for an IP address and log entry.
You can modify the ip variable to look for all entries.
"""

f = open('access.log', "r")
lines = f.readlines()
ip = '142.13.235.92'
for string in lines:
    if ip in string:
        print(string)