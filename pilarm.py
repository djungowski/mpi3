#!/usr/bin/python

import os
import sys
import logging
from alarm import threadalarm, threadweb
import signal

wakeupTime = sys.argv[1]
wakeupMusic = sys.argv[2]

if (os.path.isfile(wakeupMusic) == False):
	print 'The file "' + wakeupMusic + '" does not exist'
	sys.exit()

logging.basicConfig(level=logging.INFO)

logging.info('Starting alarm')
threadAlarm = threadalarm.ThreadAlarm("ThreadAlarm", wakeupTime, wakeupMusic, logging)
threadAlarm.start()

logging.info('Starting web interface')
threadWeb = threadweb.ThreadWeb("ThreadWeb", logging)
threadWeb.start()

def signal_handler(signal, frame):
	print 'Alarm stopped'
	threadAlarm.stopAlarm()
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

print '+++'
print 'Press Ctrl+C to stop alarm when active'
print '+++'

signal.pause()
