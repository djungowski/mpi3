import threading
import alarm
import json

class ThreadAlarm(threading.Thread):
	__alarm = None
	__logging = None
	__queue = None
	__collection = None

	def __init__(self, name, queue, logging):
		threading.Thread.__init__(self, name=name)
		self.__logging = logging
		self.__queue = queue

	def alarm(self):
		return self.__alarm
	
	def setCollection(self,collection):
		self.__collection = collection;

	def queue(self):
		return self.__queue

	def run(self):
		self.alarm = alarm.Alarm(self.__logging)
		self.__logging.info('Alarm ready')
		self.alarm.run()

	def stopAlarm(self):
		self.alarm.stop()
	
	def shutdown(self):
		self.alarm.shutdown()
	
	# Receive message from queue
	def receive(self, workload):
		self.__logging.debug(self.getName() + ":Receiving Message from Queue")
		self.__logging.debug(workload)

		pushData = None
		type = workload.get("type")
		if (type == "wakeupTime"):
			self.alarm.setWakeupTime(workload.get("value"))
			self.__pushAlarmSettings()
		elif (type == "stop"):
			self.alarm.stop()
			pushData = {"target":"web","type":"message","value":"Alarm stopped"}
		elif (type == "wakeupMusic"):
			key = int(workload.get("value"))
			music = self.__collection.get(key)
			self.alarm.setWakeupMusic(music)
			self.__pushAlarmSettings()
		elif (type == "alarm.settings"):
			self.__pushAlarmSettings()

		if (pushData != None):
			self.__queue.put(json.dumps(pushData))
	
	def __pushAlarmSettings(self):
		pushData = self.alarm.getSettings()
		pushData["target"] = "web"
		pushData["type"] = "alarm.settings"
		self.__queue.put(json.dumps(pushData))
