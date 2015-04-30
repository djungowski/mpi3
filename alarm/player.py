import re
import time
from mplayer.async import AsyncPlayer

class Player(AsyncPlayer):
	__fadeStepsize = 2
	__startVolume = 10
	__logging = None
	__playing = False
	__paused = False
	__status = 'stop'

	def __init__(self, logging):
		AsyncPlayer.__init__(self)
		self.__logging = logging

	def repeat(self, howOften):
		self.loop = howOften

	def isFileAPlaylist(self, filename):
		return (re.search('(pls|m3u)$', filename) != None)

	def load(self, filename):
		self.__logging.info(self.isFileAPlaylist(filename))
		if (self.isFileAPlaylist(filename)):
			self.loadlist(filename)
		else:
			self.loadfile(filename)

		self.__logging.info('Playing ' + filename)

	def play(self, filename):
		self.__status = 'play'
		if (self.__paused):
			self.pause()
		else:
			self.load(filename)
			self.volume = 100
			self.__playing = True

	def stop(self):
		self.__status = 'stop'
		# Unpause if paused otherwise music won't play when hitting play
		if (self.__paused):
			self.pause()
		AsyncPlayer.stop(self)
		self.volume = self.__startVolume

	def pause(self):
		self.__status = 'pause'
		if (self.__playing):
			AsyncPlayer.pause(self)
			# Always change the paused state
			if (self.__paused):
				self.__paused = False
			else:
				self.__paused = True

	def status(self):
		return self.__status

	def fadein(self, filename):
		self.__status = 'play'
		# Start music
		volume=self.__startVolume
		self.volume = volume
		# Mute so that there is no unwanted strange effect. self.load unmutes by itself
		self.mute = True
		self.load(filename)

		stepsize=self.__fadeStepsize		
		steps=(100-volume)/stepsize

		for i in range(steps):
			volume += stepsize
			self.volume = volume
			time.sleep(1)
