# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tutorial
http://twistedmatrix.com/documents/current/core/howto/servers.html

당신의 Protocol handling class는 대개 twisted.internet.protocol.Protocol을 subclass할 것이다.
대다수의 Protocol handler는 이 클래스에서 상속받거나, 이 클래스의 다른 children를 상속받을 것이다.
프로토콜 클래스의 인스턴스는 연결당 연결 요청에 의해 생성되고, 연결 종료시 사라질 것이다.
이것은  설정이 지속적으로 프로토콜상에서 유지되지 않음을 의미한다.

지속적인 설정(Persistent configuration)은  twisted.internet.protocol.Factory의 Factory 클래스에서 유지된다.

Factory의 buildProtocol 메소드는 각 새로운 연결을 위해 Procotcol을 생성하기 위해 사용된다.
일반적으로 같은 서비스를 멀티 어드레스나 멀티 포트에 제공하기 위해 유용하다.
이것이 Factory가 연결을 listen하지 않으며, 네트워크에 대해 아무것도 모르는 이유이다.
자세한 내용은 the endpoints doucmetation을 참조하거나 IReac torTCP.listenTCP와 IReactor*.listen* API를 참조하라.
http://twistedmatrix.com/documents/current/core/howto/endpoints.html
"""
from twisted.internet.protocol import Protocol


class Echo(Protocol):

    def __init__(self, factory):
        self.factory = factory

    #연결 성공시
    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "Welcome! There are currently %d open connections.\n" %
            (self.factory.numProtocols,))

    #연결 종료시
    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    #데이터 수신시
    def dataReceived(self, data):
        self.transport.write(data)

    #데이터 전송을 전부 완료하고 연결 종료
    #self.transport.loseConnection()
    #데이터 전송을 무시하고 연결 종료
    #self.transport.abortConnection()

'''
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor


class QOTD(Protocol):

    def connectionMade(self):
        self.transport.write("An apple a day keeps the doctor away\r\n")
        self.transport.loseConnection()

class QOTDFactory(Factory):
    def buildProtocol(self, addr):
        return QOTD()

# 8007 is the port you want to run under. Choose something >1024
endpoint = TCP4ServerEndpoint(reactor, 8007)
#listen에 Factor를 사용하여 QOTD를 생성.
endpoint.listen(QOTDFactory())
reactor.run()
'''

'''
#Helper Protocols
from twisted.protocols.basic import LineReceiver
#https://twistedmatrix.com/documents/16.3.0/api/twisted.protocols.basic.LineReceiver.html


class Answer(LineReceiver):

    answers = {'How are you?': 'Fine', None: "I don't know what you mean"}

    #CR-LF가 들어왔을때까지 이벤트 발생
    def lineReceived(self, line):
        if line in self.answers:
            self.sendLine(self.answers[line])
        else:
            self.sendLine(self.answers[None])
        #RawMode 전환
        setRawMode()



    #raw data가 들어왔을 때 발생
    def rawDataReceived(self, data):
        #라인 모드 전환환
        seLineMode()

from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):

    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME"

    def connectionMade(self):
        self.sendLine("What's your name?")

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            self.handle_CHAT(line)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome, %s!" % (name,))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        for name, protocol in self.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)


class ChatFactory(Factory):

    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()
'''