import threading
import json

class ThreadPlayer(threading.Thread):
	def __init__(self, name, player, collection, queue, logging):
		threading.Thread.__init__(self, name=name)
		self.__player = player
		self.__collection = collection
		self.__queue = queue
		self.__logging = logging

	def run(self):
		print("Running")

	def receive(self, workload):
		self.__logging.debug(self.getName() + ":Receiving Message from Queue")
		self.__logging.debug(workload)

		pushData = None
		type = workload.get("type")
		if (type == 'play'):
			# First: stop any alarms that could have been stopped by this
			pushData = {"target":"alarm","type":"stop","musicplaying":True}
			key = int(workload.get("value"))
			musicTuple = self.__collection.get(key)
			music = musicTuple[0] + '/' + musicTuple[1]
			self.__player.play(music)
		elif (type == "stop"):
			self.__player.stop()
			# First: stop any alarms that could have been stopped by this
			pushData = {"target":"alarm","type":"stop"}
		elif (type == "pause"):
			self.__player.pause()

		if (pushData != None):
			self.__queue.put(json.dumps(pushData))