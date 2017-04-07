# !/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.python import usage
from twisted.runner.procmon import ProcessMonitor

import time

def makeService():

    s = ProcessMonitor()
    s.threshold = 1
    s.killTime = 5
    s.minRestartDelay = 1
    s.maxRestartDelay = 5


    return s

ss = ProcessMonitor()
#ss.startService()
ss.startService()
ss.addProcess("calc.exe *32", ['c:\windows\system32\calc.exe', ])


while True:

    #ss.startProcess('calc.exe')
    time.sleep(5)
    break
    #break
ss.stopService()

ss.startService()
while True:

    #ss.startProcess('calc.exe')
    time.sleep(5)

#ss.restartAll()
#ss.startService()

