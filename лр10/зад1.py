# Описание класса Transport
class Transport:
    def __init__(self, brand, max_speed, kind):
        self.brand=brand
        self.max_speed=max_speed
        self.kind=kind
    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'
# Описание класса Car, который наследуется от класса Transport
class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand,max_speed,kind='Car')
        self.mileage=mileage
        self._gasoline_residue=gasoline_residue
    @property
    def gasoline(self):
        return f'Осталось бензина на {self._gasoline_residue} км'
    @gasoline.setter
    def __gasoline__(self, value):
        if isinstance(value, int):
            self._gasoline_residue+=value
            print(f'Объем топлива увеличен на {value} л и составляет {self._gasoline_residue} л')
        else:
            print('Ошибка заправки автомобиля')
# Описание класса Boat, который наследуется от класса Transport
class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name=owners_name
    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'
# Описание класса Plane, который наследуется от класса Transport
class Plane(Transport):
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity=capacity
    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя  {self.capacity} людей'
 # Создание объектов классов Car, Boat, Plane с передачей аргументов
car = Car('Audi', 250, 10000, 50)
boat = Boat('Yamaha', 80, 'John')
plane = Plane('Boeing', 900, 300)
# Вывод информации о каждом объекте класса
print(car)
print(boat)
print(plane)