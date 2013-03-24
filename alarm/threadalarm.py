import threading
import alarm
import json

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
	
	# Receive message from queue
	def receive(self, workload):
		self.__logging.debug(self.getName() + ":Receiving Message from Queue")
		self.__logging.debug(workload)

		type = workload.get("type")
		if (type == "wakeupTime"):
			self.alarm.setWakeupTime(workload.get("value"))
			pushData = {"target":"web","type":"message","value":"New alarm time set"}
		elif (type == "stop"):
			self.alarm.stop()
			pushData = {"target":"web","type":"message","value":"Alarm stopped"}
		elif (type == "wakeupMusic"):
			self.alarm.setWakeupMusic(workload.get("value"))
			pushData = {"target":"web","type":"message","value":"New alarm music set"}
		
		self.__queue.put(json.dumps(pushData))
