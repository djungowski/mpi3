import re
import time
from mplayer.async import AsyncPlayer

class Alarm:
	__player = None
	__wakeupTime = None
	__wakeupMusic = None
	__logging = None
	__isPlaylist = False
	__alarmTriggered = False
	__run = True

	def __init__(self, logging):
		self.__logging = logging
		self.__player = AsyncPlayer()
		self.__player.loop = 0

	def setWakeupTime(self, wakeupTime):
		self.__wakeupTime = wakeupTime
		self.__logging.info('Waking you up at ' + wakeupTime)

	def setWakeupMusic(self, music):
		self.__wakeupMusic = music
		self.__logging.info('Waking you up with: ' + music)

	def isWakeupMusicPlaylist(self):
		return (re.search('(pls|m3u)$', self.__wakeupMusic) != None)
	
	def start(self):
		if (self.isWakeupMusicPlaylist()):
			self.__player.loadlist(self.__wakeupMusic)
		else:
			self.__player.loadfile(self.__wakeupMusic)
		
		self.__logging.info('Playing ' + self.__wakeupMusic)
		self.__fadein()
	
	def __fadein(self):
		volume=10
		stepsize=2
		steps=(100-volume)/stepsize
		for i in range(steps):
			volume += stepsize
			self.__player.volume = volume
			time.sleep(1)

	def run(self):
		while self.__run:
			self.__loop()
	
	def stop(self):
		self.__player.stop()
		self.__alarmTriggered = False

	def __loop(self):
		currentTime = time.strftime('%H:%M')
		if (currentTime == self.__wakeupTime and self.__alarmTriggered == False):
			self.__logging.info('Wakeup time ' + self.__wakeupTime + ' reached. Ring Ring! :-)')
			self.__alarmTriggered = True
			self.start()
		time.sleep(10)
