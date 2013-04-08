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

		type = workload.get("type")
		if (type == 'play'):
			key = int(workload.get("value"))
			musicTuple = self.__collection.get(key)
			music = musicTuple[0] + '/' + musicTuple[1]
			self.__player.play(music)
		elif (type == "stop"):
			self.__player.stop()
			# Also stop any alarms that could have been stopped by this
			pushData = {"target":"alarm","type":"stop"}
			self.__queue.put(json.dumps(pushData))
		elif (type == "pause"):
			self.__player.pause()