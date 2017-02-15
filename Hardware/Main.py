import RPi.GPIO as GPIO
from Sensor import Sensor
import time

# ODO: Hold script when wifi is disconnected or hold post requests unil after
sensor_ultra = 0

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
    # print "Distance:" , sensor_ultra.measure_distance() , "cm"
    if sensor_ultra.measure_distance() <= 15:
        print "Shot Make"
        

    #Slow the loop
	#print "Waiting For Sensor To Settle"
    time.sleep(0.01)


init()
while True:
    loop()

exit()
