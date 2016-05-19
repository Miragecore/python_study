import socket
import sys

s= socket.socket()
s.bind(("localhost",9999))
s.listen(10)

while True:
  sc, address = s.accept()

  print address
  f = open('test.py','wb')
  while(True):
    l = sc.recv(1024)
    while (l):
      f.write(l)
      l = sc.recv(1024)
  f.close()

  sc.close()

s.close()
