"""
We need to count the number of times the ip address repeats utilizing regex
We also need to save the output to a csv file
"""


import re
from collections import Counter
import csv

logfile="access.log"

logreg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with open(logfile) as f:
    fread = f.read()
    ip_list = re.findall(logreg, fread)
    with open("ipcount.csv", "w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow(["IP_Address", "Count"])
        for k, v in Counter(ip_list).items():
            fwritercsv.writerow([k,v])