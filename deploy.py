#!/usr/bin/env python
from ftplib import FTP
import json
import sys

with open('./setting.json', 'r') as f:
    setting = json.load(f)

host = setting['ftp.host']
user = setting['ftp.username']
passwd = setting['ftp.password']

ftp = FTP(host, user, passwd)

for filename in sys.argv[1:]:
    # For avoid misstake.
    if filename.endswith('setting.json') :
        continue
    print "PUT " + filename
    # 'www/' is the public directory.
    ftp.storbinary('STOR www/' + filename, open(filename, 'r'))

ftp.quit()
