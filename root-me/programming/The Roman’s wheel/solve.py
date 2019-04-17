import socket
import time
import string

input = """irc.root-me.org:6667
test11
test11
menaeffat"""

def sendit(s):
    print '--', s
    client.send(s)

# Parse input.
ping = 'PING '
pong = 'PONG '
lines = input.split('\n')
host = lines[0].split(':')

# Connect.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host[0], int(host[1])))

# Handshake.
sendit('NICK ' + lines[1] + '\r\n')
sendit('USER ' + lines[2] + ' 0 * :' + lines[3] + '\r\n')
sendit('join #root-me_challenge\r\n')
time.sleep(1)
sendit('privmsg candy :!ep3\r\n')

x = 0


# Output and ping/pong.
while True:
    data = client.recv(2048)
    print(data)

    if ':Candy!Candy@root-me.org PRIVMSG' in data:
        z = data.split(':Candy!Candy@root-me.org PRIVMSG')[1]
        d = z.split(":")[1].strip()
        rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
        x = string.translate(d, rot13)
        sendit('privmsg candy :!ep3 -rep ' + x + '\r\n')

    if data.startswith(ping):
        resp = data.strip(ping);
        sendit(pong + resp)
        print(pong + resp)
