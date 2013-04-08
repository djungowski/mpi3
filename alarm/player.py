import re
import time
from mplayer.async import AsyncPlayer

class Player:
	__player = None
	__fadeStepsize = 2
	__startVolume = 10
	__logging = None

	def __init__(self, logging):
		self.__player = AsyncPlayer();
		self.__logging = logging

	def repeat(self, howOften):
		self.__player.loop = howOften

	def isFileAPlaylist(self, filename):
		return (re.search('(pls|m3u)$', filename) != None)

	def load(self, filename):
		if (self.isFileAPlaylist(filename)):
			self.__player.loadlist(filename)
		else:
			self.__player.loadfile(filename)

		self.__logging.info('Playing ' + filename)

	def fadein(self, filename):
		# Start music
		volume=self.__startVolume
		self.__player.volume = volume
		self.load(filename)

		stepsize=self.__fadeStepsize		
		steps=(100-volume)/stepsize

		for i in range(steps):
			volume += stepsize
			self.__player.volume = volume
			time.sleep(1)

	def stop(self):
		self.__player.stop()

	def quit(self):
		self.__player.quit()