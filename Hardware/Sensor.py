import RPi.GPIO as GPIO
import time

class Sensor:

	def __init__(self, trig_pin, echo_pin):
		self.trig_pin=trig_pin
		self.echo_pin=echo_pin
		GPIO.setup(trig_pin, GPIO.OUT)
		GPIO.setup(echo_pin, GPIO.IN)
		GPIO.output(self.trig_pin, False)

	def measure_distance(self):

		# Send the pulse
		GPIO.output(self.trig_pin, True)
		time.sleep(0.00001)
		GPIO.output(self.trig_pin, False)

		# Get the start time of the pulse
		pulse_start = time.time()
		while GPIO.input(self.echo_pin)==0:
		  pulse_start = time.time()

		# Get the end time from the pulse
		pulse_end = time.time()
		while GPIO.input(self.echo_pin)==1:
		  pulse_end = time.time()

		# Calculate the distance in centimeters
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance, 2)

		return distance

	def set_trig_pin(self, pin):
		self.trig_pin = pin
	def set_echo_pin(self, val):
		self.echo_pin = pin
	def get_trig_pin(self):
		return self.trig_pin
	def get_echo_pin(self):
		return self.echo_pin
