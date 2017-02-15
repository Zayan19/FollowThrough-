import RPi.GPIO as GPIO
from Sensor import Sensor
import time

# ODO: Hold script when wifi is disconnected or hold post requests unil after
sensor_ultra = 0
TRIG = 23

def init ():
    print "[Status] Init"
    global sensor_ultra
    # Set the GPIO mode
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    #Initialize the sensor to pins 23 and 24
    # TRIG = 23 ECHO = 24
    sensor_ultra = Sensor(20, 26)

def exit():
    print "[Status] Exit"
    GPIO.cleanup()



def loop():
    print "loop"
    GPIO.output(self.trig_pin, True)
    time.sleep(0.000001)
    GPIO.output(self.trig_pin, False)
    print "1"
    pulse_start = time.time()
    while GPIO.input(self.echo_pin)==0:
      pulse_start = time.time()
    print "2"

    pulse_end = time.time()
    while GPIO.input(self.echo_pin)==1:
      pulse_end = time.time()
    print "3"

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:" , distance , "cm"
    # if sensor_ultra.measure_distance() == 0:
    #     print "Yes"
    # else:
    #     print "no"
    #Slow the loop
	#print "Waiting For Sensor To Settle"
    time.sleep(2)


init()
while True:
    loop()

exit()
