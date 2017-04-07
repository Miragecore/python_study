import json
import subprocess
import wx
import sys
import os
from time import sleep
from pprint import pprint

with open('ExeList.json') as data_file:
    data = json.load(data_file)

    count = len(data["list"])
    
    if count < 0 :
        sys.exit("there is nothing in list")

    for pg in data["list"]:
        os.startfile(pg["path"])
        sleep(float(data["delay"]))
        #subprocess.call([pg["path"], pg["param"]])
            

#pprint(data)
#print len(data["maps"])

#data["maps"][0]["id"]  # will return 'blabla'
#data["masks"]["id"]    # will return 'valore'
#data["om_points"]      # will return 'value'

#subprocess.call(['C:\\Temp\\a b c\\Notepad.exe', 'C:\\test.txt'])
