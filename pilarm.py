#!/usr/bin/python

import os
import sys
import logging
from tornado import websocket, ioloop, web
from alarm import alarm, websocket
import threading
import signal

wakeupTime = sys.argv[1]
wakeupMusic = sys.argv[2]

if (os.path.isfile(wakeupMusic) == False):
	print 'The file "' + wakeupMusic + '" does not exist'
	sys.exit()

logging.basicConfig(level=logging.INFO)

class AlarmThread(threading.Thread):
	__alarm = None

	def run(self):
		self.__alarm = alarm.Alarm(logging)
		self.__alarm.setWakeupTime(wakeupTime)
		self.__alarm.setWakeupMusic(wakeupMusic)
		self.__alarm.run()

	def stopAlarm(self):
		self.__alarm.stop()

class WebThread(threading.Thread):
	def run(self):
		webapp = web.Application([
			(r"/websocket", websocket.WebSocket),
		])

		webapp.listen(8888)
		ioloop.IOLoop.instance().start()

threadAlarm = AlarmThread(name="ThreadAlarm")
threadWeb = WebThread(name="ThreadWeb")
threadAlarm.start()
threadWeb.start()

def signal_handler(signal, frame):
	print 'Alarm stopped'
	threadAlarm.stopAlarm()
	sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print 'Press Ctrl+C to stop alarm when active'
signal.pause()
