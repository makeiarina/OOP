class Student:
    def __init__(self, ФИ, номер_группы, успеваемость):
        self.ФИ = ФИ# Инициализация атрибута "ФИ" экземпляра класса
        self.номер_группы = номер_группы # Инициализация атрибута "номер_группы" экземпляра класса
        self.успеваемость = успеваемость# Инициализация атрибута "успеваемость" экземпляра класса

    def print_info(self):
        print(f'ФИ: {self.ФИ}')# Вывод информации об атрибуте "ФИ" экземпляра класса
        print(f'Номер группы: {self.номер_группы}')# Вывод информации об атрибуте "номер_группы" экземпляра класса
        print(f'Успеваемость: {self.успеваемость}')# Вывод информации об атрибуте "успеваемость" экземпляра класса

s1 = Student('Макей Арина', 'PO-21', '9, 10 10')# Создание экземпляра класса Student с заданными атрибутами
s2 = Student('Маникало Полина', 'PO-21', '9,9,9')# Создание экземпляра класса Student с заданными атрибутами
s3 = Student('Белуш Дарья', 'PO-21', '9,9,9')# Создание экземпляра класса Student с заданными атрибутами
s4 = Student('Аскерова Эльвира', 'PO-11', '9,9,10')# Создание экземпляра класса Student с заданными атрибутами
s5 = Student('Лужинская Мария', 'PO-21', '8,8,8')# Создание экземпляра класса Student с заданными атрибутами
s6 = Student('Капыш Вероника', 'PO-21', '8,9,8')# Создание экземпляра класса Student с заданными атрибутами
s7 = Student('Казойть Кирилл', 'PO-21', '7,8,7')# Создание экземпляра класса Student с заданными атрибутами
s8 = Student('Чайка Игорь', 'PO-21', '6,7,8')# Создание экземпляра класса Student с заданными атрибутами
s9 = Student('Котович Владислав', 'PO-21', '8,9,9')# Создание экземпляра класса Student с заданными атрибутами
s10 = Student('Мацкойть Максим', 'PO-21', '6,5,6')# Создание экземпляра класса Student с заданными атрибутами

s_list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]# Создание списка, содержащего созданные экземпляры класса Student

for student in s_list:
    student.print_info()# Вызов метода print_info() для каждого экземпляра класса Student и печать информации о студенте