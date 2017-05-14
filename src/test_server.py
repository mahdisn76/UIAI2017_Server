
import socket
from time import sleep

HOST = 'localhost'    # The remote host
PORT = 9999              # The same port as used by the server
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((HOST, PORT))
s1.sendall('REGISTER 123\n')

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((HOST, PORT))
s2.sendall('REGISTER 234\n')

sleep(1)
data = s1.recv(1024)
print 'Received', repr(data)
# sleep(2)
s1.sendall('TEST 1\n')
s1.close()
