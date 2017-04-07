
#-*-encoding:utf-8

#관리자 권한 실행!!
import sys
import os
#from pywinauto.application import Application
from pywinauto import *
import admin
import time

def Install_VLC(VLC_PATH):

    if not admin.isUserAdmin():
        admin.runAsAdmin()

    print 'VLC 설치 시작'
    try:
        os.chdir(os.path.join(os.getcwd(), os.path.dirname((sys.argv[0]))))
        app = application.Application()
        app.Start(VLC_PATH)
        app.WaitCPUUsageLower()
    except application.AppStartError as er:
        print str(er)

    try :
        language_window = app.Connect(title=u'Installer Language', class_name='#32770').Dialog
        print 'Choose Language'
        language_window[u'OK'].Click()
    except findwindows.WindowNotFoundError as er:
        InstallWindow =  app.Connect(title=u'VLC media player \uc124\uce58', class_name='#32770').Dialog
        InstallWindow[u'\ucde8\uc18cButton'].Click()
        time.sleep(0.5)
        InstallWindow[u'\uc608(&Y)Button'].Click()
        print 'Already Installed'
        exit(1)

    print 'Choose Install or Not'
    language_window[u'\ub2e4\uc74c >'].Click()

    print 'Confirm License'
    language_window[u'\ub2e4\uc74c >'].Click()

    print 'Check Component'
    language_window[u'\ub2e4\uc74c >'].Click()

    print 'Choose Install Location'
    language_window[u'\uc124\uce58'].Click()
    app.WaitCPUUsageLower()

    print 'Install End Dialog'
    language_window[u'\ub9c8\uce68'].Click()

    print 'Compelete Install'


if __name__ == "__main__":
    Install_VLC(r"./components/vlc-2.2.2-win32.exe")
