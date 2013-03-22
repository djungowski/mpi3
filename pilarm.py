#!/usr/bin/python

import os
import sys
import logging
from alarm import threadalarm, threadweb, threadqueue
import signal
import Queue

wakeupTime = sys.argv[1]
wakeupMusic = sys.argv[2]

if (os.path.isfile(wakeupMusic) == False):
	print 'The file "' + wakeupMusic + '" does not exist'
	sys.exit()

# Set up logger
if "--debug" in sys.argv or "-d" in sys.argv:
	loglevel = logging.DEBUG
else:
	loglevel = logging.INFO

logging.basicConfig(level=loglevel)

queue = Queue.Queue()

logging.info('Starting alarm')
threadAlarm = threadalarm.ThreadAlarm("alarm", wakeupTime, wakeupMusic, queue, logging)
threadAlarm.start()

logging.info('Starting web interface')
threadWeb = threadweb.ThreadWeb("web", queue, logging)
threadWeb.start()

logging.debug('Starting queue')
workerThreads = {threadAlarm.getName(): threadAlarm, threadWeb.getName(): threadWeb}
threadQueue = threadqueue.ThreadQueue("ThreadQueue", queue, workerThreads)
threadQueue.start()

def signal_handler(signal, frame):
	print 'Alarm stopped'
	threadAlarm.stopAlarm()
signal.signal(signal.SIGINT, signal_handler)

print '+++'
print 'Press Ctrl+C to stop alarm when active'
print '+++'

signal.pause()
