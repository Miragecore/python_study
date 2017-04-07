#-*-coding: utf-8 -*-

from multiprocessing import Queue, Manager, Event
import SocketServer
from ProcessControl import getProcessInfos

import json
import time

cmd = Queue()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        #dataDict = self.server.dataDict

        data = self.request.recv(1024)

        recvCmd = data[:4]
        cmd.put(recvCmd)
        print 'recv Command : ' + recvCmd

        self.request.sendall(recvCmd)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
    """
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True,
                 dataDict={}, recvque= Queue()):
        self.dataDict = dataDict
        self.recvque = recvque
        self.recvevent = Event()
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate=True)

    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True, dataDict={}):
        self.dataDict = dataDict
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate=True)
    """