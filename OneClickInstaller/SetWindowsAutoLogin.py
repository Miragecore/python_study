#-*-encoding:utf-8
import sys
import os
from pywinauto.application import Application

def SetAutoLogin():

    print '자동 로그인 설정 시작'
    try:
        app = Application().Start(r'netplwiz.exe')
        app.WaitCPUUsageLower()
    except Application.AppStartError as er:
        print str(er)

    app3 = Application().Connect(title=u'\uc0ac\uc6a9\uc790 \uacc4\uc815', class_name='#32770')
    Accountwindow = app3[u'\uc0ac\uc6a9\uc790 \uacc4\uc815']

    if Accountwindow[u'CheckBox'].GetCheckState() == 0 :
        print 'already Auto login was set'
        Accountwindow[u'\ud655\uc778'].Click()
    else :
        Accountwindow[u'\uc774 \ucef4\ud4e8\ud130 \uc0ac\uc6a9\uc790:ListView'].GetItem(0).Select()

        Accountwindow[u'CheckBox'].UncheckByClick()

        Accountwindow[u'\uc801\uc6a9(&A)'].Click()

        Accountwindow.WaitNot('enabled', timeout=3)

        app4 = Application().Connect(title=u'\uc790\ub3d9 \ub85c\uadf8\uc628', class_name='#32770')
        AutoLoginwindow = app4[u'\uc790\ub3d9 \ub85c\uadf8\uc628']

        AutoLoginwindow[u'\uc554\ud638(&P):Edit'].SetText('meta1779')
        AutoLoginwindow[u'\uc554\ud638 \ud655\uc778(&C):Edit'].SetText('meta1779')

        AutoLoginwindow[u'\ud655\uc778'].Click()

        Accountwindow.Wait('enabled', timeout=3)

        Accountwindow[u'\ud655\uc778'].Click()

if __name__ == "__main__":
    SetAutoLogin()