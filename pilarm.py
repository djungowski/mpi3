#!/usr/bin/python

import os
import sys
import logging
from tornado import websocket, ioloop, web
from alarm import alarm, websocket, threadalarm
import time
import threading
import signal

wakeupTime = sys.argv[1]
wakeupMusic = sys.argv[2]

if (os.path.isfile(wakeupMusic) == False):
	print 'The file "' + wakeupMusic + '" does not exist'
	sys.exit()

logging.basicConfig(level=logging.INFO)

class WebThread(threading.Thread):
	def run(self):
		webapp = web.Application([
			(r"/websocket", websocket.WebSocket),
		])

		webapp.listen(8888)
		ioloop.IOLoop.instance().start()

threadAlarm = threadalarm.ThreadAlarm("ThreadAlarm", wakeupTime, wakeupMusic, logging)
threadAlarm.start()

threadWeb = WebThread(name="ThreadWeb")
threadWeb.start()

def signal_handler(signal, frame):
	print 'Alarm stopped'
	threadAlarm.stopAlarm()
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print 'Press Ctrl+C to stop alarm when active'
signal.pause()
