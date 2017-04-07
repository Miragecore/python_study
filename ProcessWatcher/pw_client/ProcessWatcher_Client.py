import socket
import struct
import json
import sys
import threading
import SocketServer


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        print 'Send ' + message
        
        response = sock.recv(1024)
        while(len(response) == 0):
            response = sock.recv(1024)
            
        print "Received: {}".format(response)
        '''
        response = sock.recv(1024)
        while (len(response) == 0):
            response = sock.recv(1024)

        print "Received: {}".format(response)
        '''
    finally:
        sock.close()


#client('127.0.0.1',20301,'quit')
'''

filename = './watch.json'
data_string= ''

with open(filename, 'r') as fs:
    data = json.load(fs)
    data_string = json.dumps(data) #data serialized


ip = '172.24.250.52'
port = 20301

#update
data_len = struct.pack('I', len(data_string))
client(ip, port, 'wach' + data_len + data_string)
'''

if __name__ == "__main__":
    #if(len(sys.argv) < 1):
        #print 'need command options'
        #sys.exit(2)

    #cmd = sys.argv[1]

    #with open('watch.json', 'r') as fs:
        #data = json.load(fs)
        #watchinfo = data['watch']
        #serverinfo = data['server']
        #data_string = json.dumps(data)  # data serialized
        #ip = serverinfo['ip']
        #port = int(serverinfo['port'])

        #print 'command : ' + cmd
        #print ip
        #print port
        #data_len = struct.pack('I', len(data_string))
        #client(ip, port, cmd + data_len + data_string)
        #client('192.168.56.1', 20301, 'quit')
        while True:
            token = raw_input('Enter [Target IP]:[PORT] >>')
            tokens = token.split(':')
            if len(tokens) == 2 :
                ip = tokens[0]
                port = int(tokens[1])
                break
            else :
                pass
        #ip = '192.168.56.1'
        #port = 20301
        print 'connected to ' + ip + ':' + str(port)
        while True:
            message = raw_input('Commands >>')
            if message == 'exit':
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
                sock.sendall(message)
                if message == 'stat':
                     recv = sock.recv(1024)
                     print recv
                print 'Send ' + message
            finally:
                sock.close()











