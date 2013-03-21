#!/usr/bin/python

import os
import sys
import logging
from tornado import websocket, ioloop, web
from alarm import alarm, websocket

wakeupTime = sys.argv[1]
wakeupMusic = sys.argv[2]

if (os.path.isfile(wakeupMusic) == False):
	print 'The file "' + wakeupMusic + '" does not exist'
	sys.exit()

logging.basicConfig(level=logging.INFO)

webapp = web.Application([
	(r"/websocket", websocket.WebSocket),
])

#webapp.listen(8888)
#ioloop.IOLoop.instance().start()

pilarm = alarm.Alarm(logging)
pilarm.setWakeupTime(wakeupTime)
pilarm.setWakeupMusic(wakeupMusic)
pilarm.start()
