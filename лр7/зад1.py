class Bus:
    def __init__(self, driver_name, bus_number, route_number, brand, start_year, mileage):
        self.__driver_name = driver_name  # Инициализация имени водителя
        self.__bus_number = bus_number  # Инициализация номера автобуса
        self.__route_number = route_number  # Инициализация номера маршрута
        self.__brand = brand  # Инициализация марки автобуса
        self.__start_year = start_year  # Инициализация года выпуска
        self.__mileage = mileage  # Инициализация пробега

    @property
    def start_year(self):  # Используем декоратор @property для создания свойства start_year
        return self.__start_year  # Возвращает значение года выпуска

    @start_year.setter  # Используем декоратор @start_year.setter для определения setter метода для свойства start_year
    def start_year(self, value):  # setter метод для свойства start_year
        self.__start_year = value  # Устанавливает значение года выпуска

    @property
    def mileage(self):  # Используем декоратор @property для создания свойства mileage
        return self.__mileage  # Возвращает значение пробега

    @mileage.setter  # Используем декоратор @mileage.setter для определения setter метода для свойства mileage
    def mileage(self, value):  # setter метод для свойства mileage
        self.__mileage = value  # Устанавливает значение пробега

bus1 = Bus("Примак М.А", "6988", "A1", "Мерседес", 2010, 120000)  # Создание экземпляра класса Bus с заданными параметрами

print(bus1.start_year)  # Выводит 2010 (печать года выпуска)
print(bus1.mileage)  # Выводит 120000 (печать пробега)

bus1.start_year = 2012  # Установка нового значения года выпуска
bus1.mileage = 150000  # Установка нового значения пробега

print(bus1.start_year)  # Выводит 2012 (новый год выпуска)
print(bus1.mileage)  # Выводит 150000 (новый пробег)