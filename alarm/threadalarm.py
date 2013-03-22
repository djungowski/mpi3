import threading
import alarm

class ThreadAlarm(threading.Thread):
	__alarm = None
	__logging = None
	__wakeupTime = None
	__wakeupMusic = None

	def __init__(self, name, wakeupTime, wakeupMusic, logging):
		threading.Thread.__init__(self, name=name)
		self.__wakeupTime = wakeupTime
		self.__wakeupMusic = wakeupMusic
		self.__logging = logging

	def alarm(self):
		return self.__alarm

	def run(self):
		self.alarm = alarm.Alarm(self.__logging)
		self.alarm.setWakeupTime(self.__wakeupTime)
		self.alarm.setWakeupMusic(self.__wakeupMusic)
		self.alarm.run()

	def stopAlarm(self):
		self.alarm.stop()
