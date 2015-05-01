class Light:
	__logging = None

	def __init__(self, logging):
		self.__logging = logging

	def fadein(self):
		self.__logging.info('[Light mock] Starting fadein')

	def shutdown(self):
		self.__logging.info('[Light mock] Shutting down light')