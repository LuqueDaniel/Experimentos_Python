import json
import urllib2
import time
import sys
import os


json_url = 'https://ntp-a1.nict.go.jp/cgi-bin/json'
format_time = '%m/%d/%Y %H:%M:%S'

if sys.platform == 'win32':
    clear_command = 'cls'
else:
    clear_command = 'clear'

data = json.loads(urllib2.urlopen(json_url).read())['st']

while True:
    os.system(clear_command)

    print 'Coordinated Universal Time (UTC):', time.strftime(format_time, time.gmtime(data))
    print 'Local Standard Time (LST):', time.strftime(format_time, time.localtime(data))

    data += 1

    time.sleep(1)
