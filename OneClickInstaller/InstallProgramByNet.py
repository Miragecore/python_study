
#-*-encoding:utf-8
import json
import os
from ftplib import FTP


#with open(filename, 'r') as fs:
#    config = json.load(fs)

ftp = FTP('10.1.5.242')
ftp.login(user='meta', passwd='meta3327')

#ftp.cwd('/C-ITS')
lists = []
ftp.retrlines("LIST", lists.append)
file_list = []
ftp.retrlines("NLST", file_list.append)
for item in lists:

    tokens = item.split(' ')
    print tokens
    for token in tokens:
        if len(token) > 0:
            print token

print file_list
#cur_Path = ftp.pwd()

#for item in lists:
#    print os.path.join(cur_Path, item)