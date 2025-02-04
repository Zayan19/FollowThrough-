import Sensor
# Create a sensor handler which will track all of the data coming from a certain sensor
# params
# type: type of sensor: STRING
# sensor: a sensor object :Sensor
# cutOffVal: the value at which to compare teh sensor values to
# n: the number of values to track
class SensorHandler:
    recent_values = []
    def __init__(self, t, sensor, cutOffVal=15, n=3):
        self.type = t
        self.recent_values = []
        self.sensor = sensor
        self.cutOffVal = cutOffVal
        self.n = n

    # Update the recent values of the sensor
    def update(self):
        self.recent_values.append(self.sensor.measure_distance())
        if len(self.recent_values) > self.n:
            self.recent_values.pop(0)

    def change_pins (self, pin1, pin2):
        self.sensor.set_trig_pin(pin1)
        self.sensor.set_echo_pin(pin2)

    # Determine if all of he values in the list are under the cutoff val
    def wasShotMade(self):
        for i in self.recent_values:
            print i
        print "\n"
        if all(i < self.cutOffVal for i in self.recent_values):
            print "[EVENT] Shot made"
            return True
        return False
