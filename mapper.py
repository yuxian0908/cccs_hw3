#!/usr/bin/env python
import sys
import time
import datetime

for line in sys.stdin:
    line = line.strip()
    words = line.split('[')
    words = words[1].split(' -0800')
    time = datetime.datetime.strptime(words[0], "%d/%b/%Y:%H:%M:%S")
    print(time.strftime('%Y-%m-%d T %H:00:00.000')+"\t1")

