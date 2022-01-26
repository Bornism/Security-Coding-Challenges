"""
This is a regex log parser that specifically looks for IP addresses in an apache log file.
"""

import re


def reader(filename):
    with open(filename) as f:
        log = f.read()
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        # \d is saying its value can be between 1 to 3 and so forth (0-255).(0-225).(0-255).(0-255)
        ips_list = re.findall(regexp, log)
        print(ips_list)


if __name__ == '__main__':
    reader('/Users/christopherduncan/Documents/GitHub/SecurityCodingChallenges/Security-Coding-Challenges/access.log')