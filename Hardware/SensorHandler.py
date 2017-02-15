import Sensor
# Create a sensor handler which will track all of the data coming from a certain sensor
# params
# type: type of sensor: STRING
# sensor: a sensor object :Sensor
# cutOffVal: the value at which to compare teh sensor values to
# n: the number of values to track
class SensorHandler:
    recent_values = []
    shot_allowed = True
    def __init__(self, type, sensor, cutOffVal="15", n=3):
        self.type = t
        self.recent_values = []
        self.sensor = sensor
        self.cutOffVal = cutOffVal
        self.n = n

    # Update the recent values of the sensor
    def update(self):
        if shot_allowed:
            self.recent_values.append(sensor.measure_distance())
            if len(recent_values) >= self.n:
                recent_values.pop(0)

    # Determine if all of he values in the list are under the cutoff val
    def wasShotMade(self):
        if shot_allowed:
            if all(i < cutOffVal for i in recent_values):
                return true
        return false
