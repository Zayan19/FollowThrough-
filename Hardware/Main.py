import RPi.GPIO as GPIO
from Sensor import Sensor
from SensorHandler import SensorHandler
from ShotHandler import ShotHandler

import time
import urllib2


def init ():
    print "[STATUS] Init"
    global sensor_handler, shot_handler

    # Set the GPIO mode
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    #Initialize the sensor to pins 23 and 24
    sensor_handler = SensorHandler("distance", Sensor(20, 26))
    shot_handler = ShotHandler ("George")

# Called every time the program executes the main loop
def loop():
    global sensor_handler, shot_handler

    # update the sensor handler
    sensor_handler.update()

    if (sensor_handler.wasShotMade()):
        shot_handler.shoot()

        # sleep the thread so a shot doesnt get counted twice
        time.sleep(1.0)

    #Slow the loop
    time.sleep(0.01)

def exit():
    print "[STATUS] Exit"
    GPIO.cleanup()

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

interneton = False;
def main():
    init()

    counter = 0
    while True:

        # only check the internet every once in a while
        if (counter % 10000 == 0):
            print "[PROCESS] Begin check internet."
            interneton = internet_on()

        loop()

        counter = counter + 1

    exit()


main()
