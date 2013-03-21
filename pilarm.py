#!/usr/bin/python

import os, sys, logging, time, asyncore, re, getopt
from mplayer.async import AsyncPlayer

wakeupTime = sys.argv[1]
wakeupSong = sys.argv[2]

if (os.path.isfile(wakeupSong) == False):
	print 'The file "' + wakeupSong + '" does not exist'
	sys.exit()

isPlaylist = (re.search('(pls|m3u)$', wakeupSong) != None)

# Must put into a class! 
wakeupTriggered = False

logging.basicConfig(level=logging.INFO)
logging.info('Waking you up at ' + wakeupTime)
logging.info('Waking you up with: ' + wakeupSong)

def wakeup():
	player = AsyncPlayer()
	player.loop = 0
	if (isPlaylist):
		player.loadlist(wakeupSong)
	else:
		player.loadfile(wakeupSong)
	logging.info('Playing ' + wakeupSong)
	asyncore.loop()

def loop():
	# ugly! must put into class in next step
	global wakeupTriggered
	
	currentTime = time.strftime('%H:%M')
	if (currentTime == wakeupTime and wakeupTriggered == False):
		logging.info('Wakeup time ' + wakeupTime + ' reached. Ring Ring! :-)')
		wakeupTriggered = True
		wakeup()
	time.sleep(10)

while True:
	loop()
