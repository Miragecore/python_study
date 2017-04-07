#-*-encoding:utf-8
import sys
import os
import time
os.chdir(os.path.join(os.getcwd(), os.path.dirname((sys.argv[0]))))
from pywinauto.application import Application

print 'VLC 설치 시작'
try:
    app = Application().Start(r'vlc-2.2.2-win32.exe')
    app.WaitCPUUsageLower()
except Application.AppStartError as er:
    print str(er)

print '언어 선택'
language_window = Application().Connect(title=u'Installer Language', class_name='#32770').Dialog
language_window[u'OK'].Click()
time.sleep(0.5)

print '설치 여부 선택'
Install_page1 = Application().Connect(title=u'VLC media player \uc124\uce58', class_name='#32770').Dialog
language_window[u'\ub2e4\uc74c >'].Click()
time.sleep(0.5)

print '라이센스 확인창'

language_window[u'\ub2e4\uc74c >'].Click()
time.sleep(0.5)

print '구성요소 선택'
language_window[u'\ub2e4\uc74c >'].Click()
time.sleep(0.5)

print '설치 위치 선택'
#Install_page4 = Application().Connect(title=u'VLC media player \uc124\uce58 ', class_name='#32770').Dialog
language_window[u'\uc124\uce58'].Click()
app.WaitCPUUsageLower()

print '설치 종료'
language_window[u'\ub9c8\uce68'].Click()

print 'VLC 설치 완료'

