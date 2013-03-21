#!/usr/bin/python

import os
import sys
import logging
from alarm.alarm import Alarm

wakeupTime = sys.argv[1]
wakeupMusic = sys.argv[2]

if (os.path.isfile(wakeupMusic) == False):
	print 'The file "' + wakeupMusic + '" does not exist'
	sys.exit()

logging.basicConfig(level=logging.INFO)

alarm = Alarm(logging)
alarm.setWakeupTime(wakeupTime)
alarm.setWakeupMusic(wakeupMusic)
alarm.start()
