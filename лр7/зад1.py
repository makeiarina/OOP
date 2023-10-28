class Bus:
    def __init__(self, driver_name, bus_number, route_number, brand, start_year, mileage):
        self.__driver_name = driver_name
        self.__bus_number = bus_number
        self.__route_number = route_number
        self.__brand = brand
        self.__start_year = start_year
        self.__mileage = mileage

    @property
    def start_year(self):
        return self.__start_year

    @start_year.setter
    def start_year(self, value):
        self.__start_year = value

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        self.__mileage = value

bus1 = Bus("Примак М.А", "6988", "A1", "Мерседес", 2010, 120000)

print(bus1.start_year)  # Выводит 2010
print(bus1.mileage)  # Выводит 120000

bus1.start_year = 2012
bus1.mileage = 150000

print(bus1.start_year)  # Выводит 2012
print(bus1.mileage)  # Выводит 150000