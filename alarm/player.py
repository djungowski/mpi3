import re
import time
from mplayer.async import AsyncPlayer

class Player(AsyncPlayer):
	__fadeStepsize = 2
	__startVolume = 10
	__logging = None

	def __init__(self, logging):
		#self.__player = AsyncPlayer();
		AsyncPlayer.__init__(self)
		self.__logging = logging

	def repeat(self, howOften):
		self.loop = howOften

	def isFileAPlaylist(self, filename):
		return (re.search('(pls|m3u)$', filename) != None)

	def load(self, filename):
		if (self.isFileAPlaylist(filename)):
			self.loadlist(filename)
		else:
			self.loadfile(filename)

		self.__logging.info('Playing ' + filename)

	def fadein(self, filename):
		# Start music
		volume=self.__startVolume
		self.volume = volume
		self.load(filename)

		stepsize=self.__fadeStepsize		
		steps=(100-volume)/stepsize

		for i in range(steps):
			volume += stepsize
			self.volume = volume
			time.sleep(1)