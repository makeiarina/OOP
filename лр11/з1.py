class Transport:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    def __str__(self):
        return f"{self.name}: Capacity - {self.capacity}"
class Ship(Transport):
    def __init__(self, name, capacity, displacement):
        super().__init__(name, capacity)
        self.displacement = displacement
    def __str__(self):
        return f"{super().__str__()}, Displacement - {self.displacement}"
class PassengerTransport(Transport):
    def __init__(self, name, capacity, passenger_capacity):
        super().__init__(name, capacity)
        self.passenger_capacity = passenger_capacity
    def __str__(self):
        return f"{super().__str__()}, Passenger Capacity - {self.passenger_capacity}"
class PassengerShip(Ship, PassengerTransport):
    def __init__(self, name, capacity, displacement, passenger_capacity):
        Ship.__init__(self, name, capacity, displacement)
        PassengerTransport.__init__(self, name, capacity, passenger_capacity)
    def __str__(self):
        return f"{super().__str__()}, Passenger Capacity - {self.passenger_capacity}"
transport = Transport('Transport', 100)
print(transport)
ship = Ship('Ship', 200, 300)
print(ship)
passenger_transport = PassengerTransport('Passenger Transport', 150, 50)
print(passenger_transport)
passenger_ship = PassengerShip('Passenger Ship', 250, 400, 100)
print(passenger_ship)