import threading
from tornado import ioloop, web
import websocket

class ThreadWeb(threading.Thread):
	__logging = None
	__queue = None

	def __init__(self, name, queue, logging):
		threading.Thread.__init__(self, name=name)
		self.__logging = logging
		self.__queue = queue

	def queue(self):
		return self.queue

	def run(self):
		webapp = web.Application([
			(r"/websocket", websocket.WebSocket),
		])

		webapp.listen(8888)
		self.__logging.info('Web interface up and running')
		ioloop.IOLoop.instance().start()
	
	# Receive message from queue
	def receive(self, workload):
		self.__logging.debug(self.getName() + ":Receiving Message from Queue")
		self.__logging.debug(workload)
