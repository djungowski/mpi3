class Player:
	loop = 0
	__logging = None

	def __init__(self, logging):
		self.__logging = logging
		logging.info("Starting Player mock")

	def repeat(self, howOften):
		self.loop = howOften

	def quit(self):
		self.__logging.debug("Shutting down player mock")