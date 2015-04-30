class Player:
	loop = 0

	def __init__(self, logging):
		logging.info("Starting Player mock")

	def repeat(self, howOften):
		self.loop = howOften