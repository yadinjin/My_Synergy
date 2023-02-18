class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    

class Autobus(Transport):
    capacity = 50
    
    def __init__(self, name, max_speed, mileage, capacity):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity
        
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {self.capacity} пассажиров"

autobus = Autobus('Renault Logan',120, 15, 50)    
print(autobus.seating_capacity(autobus))