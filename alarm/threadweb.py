import threading
from tornado import ioloop, web
import websocket

class ThreadWeb(threading.Thread):
	def run(self):
		webapp = web.Application([
			(r"/websocket", websocket.WebSocket),
		])

		webapp.listen(8888)
		ioloop.IOLoop.instance().start()
