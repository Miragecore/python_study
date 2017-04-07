
#-*-encoding:utf-8

#관리자 권한 실행!!
import sys
import os
#from pywinauto.application import Application
from pywinauto import *
import admin
import time

def Install_Font(VLC_PATH):

    if not admin.isUserAdmin():
        admin.runAsAdmin()

    print '나눔 글꼴 설치 시작'
    try:
        os.chdir(os.path.join(os.getcwd(), os.path.dirname((sys.argv[0]))))
        app = application.Application()
        app.Start(VLC_PATH)
    except application.AppStartError as er:
        print str(er)

    try :
        install_window = app.Dialog
        #클릭 설치
        install_window[u'\ub2e4\uc74c >Button'].Wait("enabled", timeout=30).Click()
    except findwindows.WindowNotFoundError as er:
        print 'Can not find install window'
        exit(1)

    time.sleep(0.5)
    #클릭 확인
    #install_window[u'\ud655\uc778Button'].Click()
    #클릭 설치
    install_window[u'\uc124\uce58Button'].Wait("enabled", timeout=30).Click()

    #install_window[u'\ub098\ub214\uae00\uaf34 \uc124\uce58 \uc644\ub8ccStatic4'].Wait("exists")
    #install_window[u'\ub098\ub214\uae00\uaf34 \uc124\uce58 \uc644\ub8ccStatic4'].Wait("visible")
    #install_window[u'\ub098\ub214\uae00\uaf34 \uc124\uce58 \uc644\ub8ccStatic4'].Wait("enabled")

    #대기후 툴바 설치하기 언책
    install_window[u'\ub124\uc774\ubc84 \ud234\ubc14 \uc124\uce58\ud558\uae30CheckBox'].Wait("enabled", timeout=30).UncheckByClick()
    #[u'CheckBox2', u'\ub124\uc774\ubc84 \ud234\ubc14 \uc124\uce58\ud558\uae30',
    # u'\ub124\uc774\ubc84 \ud234\ubc14 \uc124\uce58\ud558\uae30CheckBox']

    # 웹브라우저 검색 기본값 설정 언책
    install_window[u'\ub124\uc774\ubc84\ub97c \uc6f9 \ube0c\ub77c\uc6b0\uc800\uc758 \uac80\uc0c9 \uae30\ubcf8\uac12\uc73c\ub85c \uc124\uc815\ud558\uae30CheckBox'].UncheckByClick()
    #[u'CheckBox', u'CheckBox0', u'CheckBox1', u'\ub124\uc774\ubc84\ub97c \uc6f9 \ube0c\ub77c\uc6b0\uc800\uc758 \uac80\uc0c9 \uae30\ubcf8\uac12\uc73c\ub85c \uc124\uc815\ud558\uae30', u'\ub124\uc774\ubc84\ub97c \uc6f9 \ube0c\ub77c\uc6b0\uc800\uc758 \uac80\uc0c9 \uae30\ubcf8\uac12\uc73c\ub85c \uc124\uc815\ud558\uae30CheckBox']

    #마침 클릭
    install_window[u'\ub9c8\uce68Button'].Click()
    #[u'\ub9c8\uce68', u'Button2', ]

    print '나눔 글꼴 설치 완료'





if __name__ == "__main__":
    Install_Font(r"./components/NanumFontSetup_TTF_ALL_hangeulcamp.exe")