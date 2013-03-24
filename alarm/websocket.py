from tornado import websocket
import json

class WebSocket(websocket.WebSocketHandler):
	__queue = None

	def initialize(self, queue, listeners):
		self.__queue = queue
		for key in listeners:
			listeners[key].socket = self

	def open(self):
		print "WebSocket opened"

	def on_message(self, message):
		self.__queue.put(message)

	def on_close(self):
		print "WebSocket closed"

	def send(self, message):
		self.write_message(message)
