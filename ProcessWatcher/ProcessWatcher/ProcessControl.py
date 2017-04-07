#-*-coding: utf-8 -*-

"""@packeage
 Process Control Module
 - Process Monitoring (Check status : running, not running, not response)
 - Process Start
 - Process Stop
"""

import os
import locale
import subprocess
from datetime import datetime

# k = os.popen('taskkill /F /T /PID %s' % i).read()
def write_log(msg):
    log_path = './log'
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    str_logfileName = datetime.now().strftime('%y%m%d') + '.log'
    str_logfileName = os.path.join(log_path, str_logfileName)
    str_time = '[' + datetime.now().strftime("%H:%M:%S") + '] : '
    with open(str_logfileName, 'a+') as fp:
        fp.write(str_time + msg + '\n')


def getProcessInfos(processInfos):
    """
    Check Process Status
    :return: Process running status dictionary
    """
    for key in processInfos.keys():
        processInfos[key]['response'] = 'NotRun'
        processInfos[key]['pid'] = '-'

    r = os.popen('tasklist /FI "STATUS eq Running"').read().strip().split('\n')

    for p in r:
        d = p.split(' ')
        proc_name = d.pop(0)

        if not proc_name.__contains__('exe'):
            continue
        #print 'pp: ' + proc_name
        bFound  = False
        for proc_list_item in processInfos.keys():
            #print proc_list_item
            if not proc_name.startswith(proc_list_item):
                continue
            else:
                bFound = True
        if not bFound:
            continue
        #print 't2'
        pid = d.pop(0)
        while not pid:
            pid = d.pop(0)
        #print processInfos.keys()
        #print 't1'

        #proc_status = {'pid': pid, 'response': True}
        #processInfos[proc_name] = proc_status
        processInfos[proc_name]['pid'] = pid
        processInfos[proc_name]['response'] = 'Running'
        #print "processName : %s, pid: %s, response : Running" % (proc_name, pid)

    r = os.popen('tasklist /FI "STATUS eq Not Responding"').read().strip().split('\n')

    for p in r:
        d = p.split(' ')
        proc_name = d.pop(0)
        if not proc_name.__contains__('exe'):
            continue
        bFound = False
        for proc_list_item in processInfos.keys():
            if not proc_name.startswith(proc_list_item):
                continue
            else:
                bFound = True
        if not bFound:
            continue

        pid = d.pop(0)
        while not pid:
            pid = d.pop(0)

        #proc_status = {'pid': pid, 'response': False}
        processInfos[proc_name]['pid'] = pid
        processInfos[proc_name]['response'] = 'NotResponse'
        #print "processName : %s, pid: %s, response : NotResponse" % (proc_name, pid)

    bOk = True
    for proc_name in processInfos.keys():
        if processInfos[proc_name]['response'] != 'Running':
            bOk = False
            print "ProcessName : %s, PID: %s, Status : %s" % (proc_name,
                                                             processInfos[key]['pid'],
                                                             processInfos[key]['response'])

            write_log("ProcessName : %s, PID: %s, Status : %s" % (proc_name,
                                                             processInfos[key]['pid'],
                                                             processInfos[key]['response']))
    if bOk:
        write_log("All Processes Works Properly")
        print "All Processes Works Properly"


def startNewProcess(start_command, path):
    """
    :param start_command:
    :param path:
    :return: None
    """
    try:
        subprocess.Popen(start_command, bufsize=-1, cwd=path, creationflags=subprocess.CREATE_NEW_CONSOLE)
    except subprocess.CalledProcessError:
        print 'Can not Start Command : \'%s\'' % start_command
        write_log('Can not Start Command : \'%s\'' % start_command)
        pass
    except WindowsError:
        print 'Can not Excute start_Command : \'%s\'' % start_command
        write_log('Can not Excute start_Command : \'%s\'' % start_command)
        pass

def killProcess(pid):
    """

    :param pid:
    :return:
    """

    localeInfo = locale.getdefaultlocale()
    resultMsg = os.popen('taskkill /F /T /PID %s' % pid).read()
    resultMsg = resultMsg.decode(localeInfo[1]).encode('utf8')
    print resultMsg
    return resultMsg

def watchNBiteProcess(config):
    #processName = config['name']
    #if processName in processInfos:
        #if not processInfos[processName]['response']:
    if config['response'] == 'NotResponse':
        killProcess(config['pid'])
    if config['response'] == 'NotRun':
        startNewProcess(config['startCmd'], config['path'])

def do_Monitor(config):
    getProcessInfos(config)
    for key in config.keys():
        watchNBiteProcess(config[key])

def do_killAll(config):
    getProcessInfos(config)
    for key in config.keys():
        if config[key]['response'] != 'NotRun':
            print "Process %s, response: %s" % (config[key]['name'], config[key]['response'])
            write_log("Process %s, response: %s" % (config[key]['name'], config[key]['response']))
            killProcess(config[key]['pid'])


