class Transport:#Создание базового класса Transport.
    def __init__(self, name, capacity):#Определение метода инициализации класса с параметрами name (наименование) и capacity (вместимость).
        self.name = name
        self.capacity = capacity
    def __str__(self):#Определение метода для вывода информации об объекте.
        return f"{self.name}: Capacity - {self.capacity}"
class Ship(Transport):#Создание класса Ship, который наследуется от класса Transport.
    def __init__(self, name, capacity, displacement):#Определение метода инициализации класса Ship с дополнительным параметром displacement (водоизмещение).
        super().__init__(name, capacity)
        self.displacement = displacement
    def __str__(self):#Переопределение метода str для добавления информации о водоизмещении.
        return f"{super().__str__()}, Displacement - {self.displacement}"
class PassengerTransport(Transport):#Создание класса PassengerTransport, также наследующего от базового класса Transport.
    def __init__(self, name, capacity, passenger_capacity):# Определение метода инициализации класса PassengerTransport с параметром passenger_capacity (пассажирская вместимость).
        super().__init__(name, capacity)
        self.passenger_capacity = passenger_capacity
    def __str__(self):#Переопределение метода str для вывода дополнительной информации о пассажирской вместимости.
        return f"{super().__str__()}, Passenger Capacity - {self.passenger_capacity}"
class PassengerShip(Ship, PassengerTransport):#Создание класса PassengerShip, который наследуется и от класса Ship, и от класса PassengerTransport.
    def __init__(self, name, capacity, displacement, passenger_capacity):#Метод инициализации класса PassengerShip, расширяющий функционал двух родительских классов.
        Ship.__init__(self, name, capacity, displacement)
        PassengerTransport.__init__(self, name, capacity, passenger_capacity)
    def __str__(self):#Переопределение метода str для вывода информации о пассажирской вместимости и других характеристиках.
        return f"{super().__str__()}, Passenger Capacity - {self.passenger_capacity}"
transport = Transport('Transport', 100)#Создание объекта transport класса Transport с параметрами 'Transport' и 100.
print(transport)#Вывод информации о созданном объекте.
ship = Ship('Ship', 200, 300)#Создание объекта ship класса Ship с параметрами 'Ship', 200 и 300.
print(ship)#Вывод информации о созданном объекте.
passenger_transport = PassengerTransport('Passenger Transport', 150, 50)#Создание объекта passenger_transport класса PassengerTransport с параметрами 'Passenger Transport', 150 и 50.
print(passenger_transport)#Вывод информации о созданном объекте.
passenger_ship = PassengerShip('Passenger Ship', 250, 400, 100) #Создание объекта passenger_ship класса PassengerShip с параметрами 'Passenger Ship', 250, 400 и 100.
print(passenger_ship)#Вывод информации о созданном объекте.