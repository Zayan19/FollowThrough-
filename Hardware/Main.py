import RPi.GPIO as GPIO
from Sensor import Sensor
import time
import urllib2

sh = 0

def init ():
    print "[STATUS] Init"
    global sh

    # Set the GPIO mode
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    #Initialize the sensor to pins 23 and 24
    sh = SensorHandler(Sensor(20, 26))

recent_values = []
# Called every time the program executes the main loop
def loop():
    global sh

    # update the sensor handler
    sh.update()

    if (sh.wasShotMade()):
        print "[EVENT] Shot made"
        sh.shoot()
        time.sleep(0.25)

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
