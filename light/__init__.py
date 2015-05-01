import time

class Light:
	__leds = 50
	__channels = 0
	__buffer = None
	__spidev = None
	__stepsize = 36
	__logging = None

	def __init__(self, logging):
		self.__logging = logging
		self.__channels = self.__leds * 3  # Each LED has 3 bythes for rgb
		self.__buffer = bytearray(self.__channels)
		self.__spidev = file("/dev/spidev0.0", "wb")

		self.__init_buffer()

	def __init_buffer(self):
		for i in range(self.__channels):
			self.__buffer[i] = 0x00
		self.__flush_buffer()


	def __flush_buffer(self):
		self.__spidev.write(self.__buffer)
		self.__spidev.flush()
		time.sleep(0.0005)

	def fadein(self):
		self.__logging.info('Fadeing in light')
		for i in range(self.__leds):
			led_offset = i * 3
			self.__logging.debug('Activating LED #' + str((i + 1)))
			self.__logging.debug('LED Byte Offset: ' + str(led_offset))

			red = led_offset
			green = led_offset + 1
			blue = led_offset + 2
			self.__buffer[red] = 0xFF
			self.__buffer[green] = 0xFC
			self.__buffer[blue] = 0x00
			self.__flush_buffer()
			time.sleep(self.__stepsize)

	def shutdown(self):
		self.__logging.info('Shutting down light')
		self.__init_buffer()
