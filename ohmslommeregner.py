from math import sqrt

class OhmsLov:
    
    def __init__(self, current, power, resistance, voltage):
        self.current = current
        self.power = power
        self.voltage = voltage
        self.resistance = resistance
        
     # current   
    def current_calc(self):
        current = 0
        current = self.voltage / self.resistance
        print(current)
    
    def current_calc1(self):
        current = 0
        current = sqrt(self.power / self.resistance)
        print(current)
    
    def current_calc2(self):
        current = 0
        current = self.power / self.voltage
        print(current)
    
    # resistance
    def resistance_calc(self):
        resistance = 0
        resistance = self.voltage / self.current
        print(resistance)
    
    def resistance_calc1(self):
        resistance = 0
        resistance = self.power / self.current**2
        print(resistance)
    
    def resistance_calc2(self):
        resistance = 0
        resistance = self.voltage**2 / self.power
        print(resistance)
    
    # voltage
    def voltage_calc(self):
        voltage = 0
        voltage = self.power / self.current
        print(voltage)
    
    def voltage_calc1(self):
        voltage = 0
        voltage = sqrt(self.power / self.resistance)
        print(voltage)
    
    def voltage_calc2(self):
        voltage = 0
        voltage = self.voltage / self.resistance
        print(voltage)
    
    # power
    def power_calc(self):
        power = 0
        power = self.voltage * self.current
        print(power)
        
    def power_calc1(self):
        power = 0
        power = self.voltage**2 / self.resistance
        print(power)
    
    def power_calc2(self):
        power = 0
        power = self.resistance * self.current**2
        print(power)
        
        
calc = OhmsLov(200, 5, 0, 0)

#calc.current_calc()
#calc.current_calc1()
#calc.current_calc2()
#calc.resistance_calc()
#calc.resistance_calc1()
#calc.resistance_calc2()
calc.voltage_calc()
#calc.voltage_calc1()
#calc.voltage_calc2()
#calc.power_calc()
#calc.power_calc1()
#calc.power_calc2()










        
        
        