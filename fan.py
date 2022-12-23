from RPi import GPIO


class Fan:
	'''Управление вентилятором'''
	GPIO.setmode(GPIO.BCM)
	is_enable = False

	def __init__(self, control_pin):
		self.control_pin = control_pin
		GPIO.setup(self.control_pin, GPIO.OUT, initial=0)

	def enable(self):
		'''Включить вентилятор'''
		GPIO.output(self.control_pin, True)
		self.is_enable = True

	def disable(self):
		'''Выключить вентилятор'''
		GPIO.output(self.control_pin, False)
		self.is_enable = False

	def __del__(self):
		GPIO.cleanup()
