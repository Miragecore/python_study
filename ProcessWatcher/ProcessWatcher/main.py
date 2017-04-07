#-*-coding: utf-8 -*-

from multiprocessing import Process, Queue, Manager
from ProcessControl import do_Monitor,do_killAll, getProcessInfos
from server import ThreadedTCPRequestHandler, ThreadedTCPServer
import socket
import threading
import time
import json
from server import cmd

if __name__=='__main__':
    print 'start watcher Ver. 1.0.0'
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 20301

    filename = './monitor.json'
    data_string = ''
    config = {}
    with open(filename, 'r') as fs:
        config = json.load(fs)
        # data_string = json.dumps(data)  # data serialized

    #manager = Manager()
    #dataDict = manager.dict()
    #dataDict = manager.dict(config)

    #dataDict['opCode'] = 'strt'
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler, True)
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    ip, port = server.server_address
    print 'starting Watching server IP ' + ip, port
    # print ip, port
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()

    isMonitor = True
    opCode = 'strt'
    while isMonitor:
        if not cmd.empty():
            opCode = cmd.get()

        if opCode == 'strt':
            do_Monitor(config['processes'])

        if opCode == 'kill':
            do_killAll(config['processes'])
            #opCode = 'stop'

        if opCode == 'stop':
            getProcessInfos(config['processes'])

        if opCode == 'quit':
            do_killAll(config['processes'])
            isMonitor = False

        time.sleep(15)

    server.shutdown()
    server.server_close()
    server_thread.join()

    print 'end'
