#!/usr/bin/python

import os
import sys
import logging
from alarm import threadalarm, threadweb, threadqueue, threadplayer
if "--mock-player" in sys.argv:
	from mock import player
else:
	from alarm import player
import signal
import Queue
import ConfigParser
if "--mock-light" in sys.argv:
	from mock.light import Light
else:
	from light import Light
from scan import music

# Set up logger
if "--debug" in sys.argv:
	loglevel = logging.DEBUG
else:
	loglevel = logging.INFO

logging.basicConfig(level=loglevel)

logging.debug('Reading config')
config = ConfigParser.ConfigParser()
config.read(os.getcwd() + "/config.ini")

daemon = 0

if "-d" in sys.argv:
	fpid = os.fork()
	if fpid != 0:
		logging.info('Running as daemon');
		pidfile = open(config.get('general', 'pid'), 'w')
		pidfile.write(str(fpid))
		# Running as daemon now. PID is fpid
		sys.exit(0)

musicPaths = config.items("paths")
logging.info('Scanning music collection')
logging.debug(musicPaths)
collection = music.Music(musicPaths)
collection.scan()
logging.info('Scanning finished. Found ' +  str(collection.count()) + ' items')

queue = Queue.Queue()

logging.info('Starting player')
player = player.Player(logging)
threadPlayer = threadplayer.ThreadPlayer("player", player, collection, queue, logging)
threadPlayer.start()

light = Light()
logging.info('Starting alarm')
threadAlarm = threadalarm.ThreadAlarm("alarm", player, queue, logging)
threadAlarm.setCollection(collection)
threadAlarm.set_light(light)
threadAlarm.start()

port = config.get('http', 'port')
logging.info('Starting web interface')
threadWeb = threadweb.ThreadWeb("web", port, queue, logging)
threadWeb.setCollection(collection)
threadWeb.start()

logging.debug('Starting queue')
workerThreads = {threadAlarm.getName(): threadAlarm, threadWeb.getName(): threadWeb, threadPlayer.getName(): threadPlayer}
threadQueue = threadqueue.ThreadQueue("ThreadQueue", queue, workerThreads, logging)
threadQueue.start()

def signal_handler(signal, frame):
	logging.info('Shutting down alarm')
	threadAlarm.shutdown()
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

signal.pause()
