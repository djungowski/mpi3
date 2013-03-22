import threading
import alarm

class ThreadAlarm(threading.Thread):
	__alarm = None
	__logging = None
	__wakeupTime = None
	__wakeupMusic = None
	__queue = None

	def __init__(self, name, wakeupTime, wakeupMusic, queue, logging):
		threading.Thread.__init__(self, name=name)
		self.__wakeupTime = wakeupTime
		self.__wakeupMusic = wakeupMusic
		self.__logging = logging
		self.__queue = queue

	def alarm(self):
		return self.__alarm

	def queue(self):
		return self.__queue

	def run(self):
		self.alarm = alarm.Alarm(self.__logging)
		self.alarm.setWakeupTime(self.__wakeupTime)
		self.alarm.setWakeupMusic(self.__wakeupMusic)
		self.__logging.info('Alarm ready')
		self.alarm.run()

	def stopAlarm(self):
		self.alarm.stop()
