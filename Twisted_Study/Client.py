# !/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import Protocol
from sys import stdout

class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)