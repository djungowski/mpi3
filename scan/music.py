import os
import re

class Music:
	__paths = []
	__music = []
	__supportedFiles = ("mp3", "ogg", "wav", "ac3", "pls", "m3u", "flac")

	def __init__(self, paths):
		self.__paths = paths

	def scan(self):
		for key, path in self.__paths:
			self.__walkFolder(path)
	
	def __walkFolder(self, folder):
		items = os.listdir(folder)
		for filename in items:
			self.__scanFile(folder, filename)
	
	def __scanFile(self, folder, filename):
		file = folder + '/' + filename
		if (os.path.isdir(file)):
			self.__walkFolder(file)
		else:
			if self.isSupportedFile(filename):
				self.__music.append((folder, filename))	

	def isSupportedFile(self, file):
		supportedFiles = "|".join(self.__supportedFiles)
		return re.search('.' + supportedFiles + '$', file) != None

	def getAll(self):
		return self.__music

	def get(self, index):
		return self.__music[index]

	def count(self):
		return len(self.__music)
