import threading
import Queue
import json

class ThreadQueue(threading.Thread):
	__queue = None
	__threads = {}
	__logging = None

	def __init__(self, name, queue, threads, logging):
		threading.Thread.__init__(self, name=name)
		self.__threads = threads
		self.__queue = queue
		self.__logging = logging

	def threads(self):
		return self.__threads
		
	def queue(self):
		return self.__queue

	def run(self):
		while True:
			workload = json.loads(self.__queue.get())
			self.__logging.debug('Queue received workload')
			self.__logging.debug(workload)
			target = workload.get("target")
			targetThread = self.threads().get(target)
			if (targetThread != None):
				targetThread.receive(workload)
