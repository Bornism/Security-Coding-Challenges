"""
Author: Christopher Duncan
Build Date: 01/06/2022
This project is a ssh botnet. SSH is an encrypted remote terminal connection. Which allows command line access
to the device. I learned how to build this SSH botnet via a video but I have created my own in my liking for my
own understanding.

What is a botnet? -
A botnet (derived from 'robot network') is a large group of malware-infected internet-connected devices
and computers controlled by a single operator.
Attackers use these compromised devices to launch large-scale attacks to disrupt services,
steal credentials and gain unauthorized access to critical systems.

Steps for the SSH Botnet:
1. We'll be using the pexpect library with the pxssh module to connect to the SSH server
2. We then store that connection and leave it waiting for a command
3. We send a command to all of the connections open in the botnet

"""


from pexpect import pxssh


class SSHClient:

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            c = pxssh.pxssh()
            c.login(self.hostname, self.username, self.password)
            return c
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# The methods defined below are global and not static hence why we don't see the self mentioned as a parameter.
def botnetcommand(command):
    for client in botNet:
        output = client.send_command(command)
        print('[*] Output from ' + client.host)
        print('[*]' + output)


def addclient(hostname, username, password):
    client = SSHClient(hostname, username, password)
    botNet.append(client)


botNet = []
addclient('127.0.0.1', 'apples12', 'ilikeoranges12')

botnetcommand('df -h')
