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

logging.basicConfig(level=logging.INFO)

queue = Queue.Queue()

logging.info('Starting alarm')
threadAlarm = threadalarm.ThreadAlarm("ThreadAlarm", wakeupTime, wakeupMusic, queue, logging)
threadAlarm.start()

logging.info('Starting web interface')
threadWeb = threadweb.ThreadWeb("ThreadWeb", queue, logging)
threadWeb.start()

logging.debug('Starting queue')
workerThreads = {threadAlarm.getName(): threadAlarm, threadWeb.getName(): threadWeb}
threadQueue = threadqueue.ThreadQueue("ThreadQueue", queue, workerThreads)
threadQueue.start()

def signal_handler(signal, frame):
	print 'Alarm stopped'
	threadAlarm.stopAlarm()
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

print '+++'
print 'Press Ctrl+C to stop alarm when active'
print '+++'

signal.pause()
