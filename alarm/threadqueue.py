import threading
import Queue
import json

class ThreadQueue(threading.Thread):
	__queue = None
	__threads = {}

	def __init__(self, name, queue, threads):
		threading.Thread.__init__(self, name=name)
		self.__threads = threads
		self.__queue = queue

	def threads(self):
		return self.__threads
		
	def queue(self):
		return self.__queue

	def run(self):
		self.queue.put('{}')
		while True:
			workload = json.loads(self.__queue.get())
			print(workload)
