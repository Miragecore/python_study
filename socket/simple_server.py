from socket import *
from select import *
import sys
from time import ctime

HOST_IP = '127.0.0.1'
HOST_PORT = 56789
ADDR = (HOST_IP, HOST_PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(ADDR)

serverSocket.listen(10)

connection_list = [serverSocket]

print('Server Start')
print('port : %s' % str(HOST_PORT))

while connection_list:
  try:
    print('wait for connection')
    read_socket, write_socket, error_socket = select(connection_list,
                                                     [], [], 10)
    for sock in read_socket:
      #new connection
      if sock == serverSocket:
        clientSocket, addr_info = serverSocket.accept()
        connection_list.append(clientSocket)
        print('%s : IP : %s' % (ctime(), addr_info[0]))
      #receive data from client
      else :
        data = sock.recv(1024)
        print('receive data')

  except KeyboardInterrupt:
    serverSocket.close()
    sys.exit()






