import threading
from tornado import ioloop, web
import websocket
import os

class CollectionListener:
	__socket = None

	def socket(self, socket):
		self.__socket = socket
	
	def send(self, message):
		self.__socket.send(message)

class ThreadWeb(threading.Thread):
	__logging = None
	__queue = None
	__collection = None
	__listeners = {}

	def __init__(self, name, queue, logging):
		threading.Thread.__init__(self, name=name)
		self.__logging = logging
		self.__queue = queue
		self.__listeners = {
			"collection": CollectionListener()
		}

	def queue(self):
		return self.__queue

	def run(self):
		webapp = web.Application([
			(r"/websocket", websocket.WebSocket, {"queue":self.__queue, "listeners":self.__listeners}),
			(r"/", web.RedirectHandler, {"url": "/index.html"}),
			(r"/(.*)", web.StaticFileHandler, {"path": os.getcwd() + "/public/"}),
		])

		webapp.listen(80)
		self.__logging.info('Web interface up and running')
		ioloop.IOLoop.instance().start()
	
	# Receive message from queue
	def receive(self, workload):
		self.__logging.debug(self.getName() + ":Receiving Message from Queue")
		self.__logging.debug(workload)

		if (workload.type == "collection.list"):
			self.__dispatcher
		
	def collection(self, collection):
		self.__collection = collection
