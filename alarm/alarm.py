import time

class Alarm:
	__player = None
	__wakeupTime = None
	__wakeupMusic = None
	__logging = None
	__isPlaylist = False
	__alarmTriggered = False
	__run = True
	__startVolume = 10

	def __init__(self, player, logging):
		self.__logging = logging
		#self.__player = AsyncPlayer()
		self.__player = player
		# Loop indefinitely
		self.__player.repeat(0)

	def setWakeupTime(self, wakeupTime):
		self.__wakeupTime = wakeupTime
		self.__logging.info('Waking you up at ' + wakeupTime)

	def setWakeupMusic(self, music):
		self.__wakeupMusic = music
		self.__logging.info('Waking you up with: ' + self.getWakeupMusicFile())
	
	def getWakeupMusicFile(self):
		return self.__wakeupMusic[0] + '/' + self.__wakeupMusic[1]
	
	def getSettings(self):
		return {
			"time":self.__wakeupTime,
			"music":self.__wakeupMusic
		}
	
	def start(self):
		music = self.getWakeupMusicFile()
		self.__player.fadein(music)

	def run(self):
		while self.__run:
			self.__loop()
	
	def stop(self):
		self.__player.stop()
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
