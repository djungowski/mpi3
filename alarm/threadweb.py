import threading
from tornado import ioloop, web
import websocket
import os
import json

class WebSocketListener:
	__socket = None

	def setSocket(self, socket):
		self.__socket = socket
	
	def send(self, message):
		self.__socket.send(json.dumps(message))

class CollectionListener(WebSocketListener):
	__collection = None

	def __init__(self, collection):
		self.__collection = collection
	
	def list(self):
		pushData = {
			"type":"collection.list",
			"data":self.__collection.getAll()
		}
		self.send(pushData)

class ThreadWeb(threading.Thread):
	__logging = None
	__queue = None
	__collection = None
	__listeners = {}
	__port = None

	def __init__(self, name, port, queue, logging):
		threading.Thread.__init__(self, name=name)
		self.__logging = logging
		self.__queue = queue
		self.__port = port
		self.__listeners = {
			"message": WebSocketListener(),
			"alarm.settings": WebSocketListener()
		}

	def queue(self):
		return self.__queue

	def run(self):
		webapp = web.Application([
			(r"/websocket", websocket.WebSocket, {"queue":self.__queue, "listeners":self.__listeners}),
			(r"/", web.RedirectHandler, {"url": "/index.html"}),
			(r"/(.*)", web.StaticFileHandler, {"path": os.getcwd() + "/public/"}),
		])

		webapp.listen(self.__port)
		self.__logging.info('Web interface up and running on port ' + str(self.__port))
		ioloop.IOLoop.instance().start()
	
	# Receive message from queue
	def receive(self, workload):
		self.__logging.debug(self.getName() + ":Receiving Message from Queue")
		self.__logging.debug(workload)

		type = workload.get("type")
		if type == "collection.list":
			self.__listeners.get("collection").list()
		else:
			self.__listeners.get("message").send(workload)
		
	def setCollection(self, collection):
		self.__collection = collection
		self.__listeners["collection"] = CollectionListener(collection)
