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
	__startVolume = 10

	def __init__(self, logging):
		self.__logging = logging
		self.__player = AsyncPlayer()
		self.__player.loop = 0

	def setWakeupTime(self, wakeupTime):
		self.__wakeupTime = wakeupTime
		self.__logging.info('Waking you up at ' + wakeupTime)

	def setWakeupMusic(self, music):
		self.__wakeupMusic = music
		self.__logging.info('Waking you up with: ' + self.getWakeupMusicFile())
	
	def getWakeupMusicFile(self):
		return self.__wakeupMusic[0] + '/' + self.__wakeupMusic[1]

	def isWakeupMusicPlaylist(self):
		return (re.search('(pls|m3u)$', self.getWakeupMusicFile()) != None)
	
	def getSettings(self):
		return {
			"time":self.__wakeupTime,
			"music":self.__wakeupMusic
		}
	
	def start(self):
		music = self.getWakeupMusicFile() 
		if (self.isWakeupMusicPlaylist()):
			self.__player.loadlist(music)
		else:
			self.__player.loadfile(music)
		
		self.__logging.info('Playing ' + music)
		self.__fadein()
	
	def __fadein(self):
		volume=self.__startVolume
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
		self.__player.volume = self.__startVolume
		self.__alarmTriggered = False

	def shutdown(self):
		self.__alarmTriggered = False
		self.__run = False
		self.__player.quit()

	def __loop(self):
		currentTime = time.strftime('%H:%M')
		if (currentTime == self.__wakeupTime and self.__alarmTriggered == False):
			self.__logging.info('Wakeup time ' + self.__wakeupTime + ' reached. Ring Ring! :-)')
			self.__alarmTriggered = True
			self.start()
		time.sleep(10)
