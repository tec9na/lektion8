class SensorClassExample:
    description = "Class to measure sensor data"
    
    def __init__(self):
        self.temperature = None
        self.humidity = None
        
    def set_temperature(self, measured_temperature):
        self.temperature = measured_temperature
        
sensor = SensorClassExample()
sensor.set_temperature(33)

print(SensorClassExample.description)
print(sensor.temperature)