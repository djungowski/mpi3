class Player:
	loop = 0
	__logging = None
	__status = 'stop'

	def __init__(self, logging):
		self.__logging = logging
		logging.info('[Player Mock] Starting Player mock')

	def play(self, filename):
		self.__status = 'play'
		self.__logging.info('[Player Mock] Playing ' + filename)

	def stop(self):
		self.__status = 'stop'
		self.__logging.info('[Player Mock] Stopping Playback')

	def pause(self):
		self.__status = 'pause'
		self.__logging.info('[Player Mock] Pausing playback')

	def repeat(self, howOften):
		self.loop = howOften

	def fadein(self, filename):
		self.__logging.info('[Player Mock] Fading in ' + filename)

	def quit(self):
		self.__logging.info('[Player Mock] Shutting down player mock')

	def status(self):
		return self.__status