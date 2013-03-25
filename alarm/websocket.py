from tornado import websocket
import json

class WebSocket(websocket.WebSocketHandler):
	connections = []
	__queue = None

	def initialize(self, queue, listeners):
		self.__queue = queue
		for key in listeners:
			listeners[key].setSocket(self)

	def open(self):
		WebSocket.connections.append(self)
		print WebSocket.connections

	def on_message(self, message):
		self.__queue.put(message)

	def on_close(self):
		WebSocket.connections.remove(self)
		print WebSocket.connections

	def send(self, message):
		for connection in self.connections:
			connection.write_message(message)
