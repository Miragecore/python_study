import socket

HOST = "127.0.0.1"
PORT = 11000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = input("Press some key")
s.close()






