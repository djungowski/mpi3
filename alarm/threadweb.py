import threading
from tornado import ioloop, web
import websocket

class ThreadWeb(threading.Thread):
	__logging = None

	def __init__(self, name, logging):
		threading.Thread.__init__(self, name=name)
		self.__logging = logging

	def run(self):
		webapp = web.Application([
			(r"/websocket", websocket.WebSocket),
		])

		webapp.listen(8888)
		self.__logging.info('Web interface up and running')
		ioloop.IOLoop.instance().start()
