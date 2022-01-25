"""
Author: Christopher Duncan
Build Date: 01/06/2022
We will be making a simple scanner that will take a given address as input, an IP address and a list of ports and
then it will try to make a tcp connection to the port and look for a response from that particular server and
if it gets a response it will let us know if the port is open on that particular server.

https://www.youtube.com/watch?v=bH-3PuQC_n0
"""
from socket import *


def connectscan(targethost, targetport):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((targethost,targetport))
        print('[+]%d/tcp open'%targetport)
        connskt.close()
    except:
        print('[-]%d/tcp closed'%targetport)


def portscan(targethost, targetports):
    try:
        targetIP = gethostbyname(targethost)
    except:
        print('[-] Cannot resolve %d' % targethost)
        return
    try:
        targetname = gethostbyaddr(targetIP)
        print('\n[+] Scan result of: %d' % targetname[0])
    except:
        print('\n[+] Scan result of: %d' % targetIP)
    setdefaulttimeout(1) # So we only do this once a second.
    for targetport in targetports:
        print('Scanning Port: ' + targetport)
        connectscan(targethost, int(targetport))


if __name__ == '__main__':
    # connectscan('142.250.9.138', 22)
    portscan('google.com', [80,22] )
