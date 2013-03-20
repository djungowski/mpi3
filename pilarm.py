#!/usr/bin/python

import os, sys, logging, time, asyncore

from mplayer.async import AsyncPlayer

wakeupTime = sys.argv[1]
wakeupSong = sys.argv[2]

# Must put into a class! 
playing = False

logging.basicConfig(level=logging.INFO)
logging.info('Waking up at ' + wakeupTime)
logging.info('Waking you up with: ' + wakeupSong)

def wakeup():
	player = AsyncPlayer()
	player.loadfile(wakeupSong)
	asyncore.loop()

def loop():
	# ugly! must put into class in next step
	global playing
	
	currentTime = time.strftime('%H:%M')
	if (currentTime == wakeupTime and playing == False):
		logging.info('Wakeup time ' + wakeupTime + ' reached. Ring Ring! :-)')
		playing = True
		wakeup()
	time.sleep(10)

while True:
	loop()
