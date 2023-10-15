class Rectangle:#Создаем класс с именем Прямоугольник
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_info(self):
        print(f'длина: {self.length}\nширина: {self.width}')
    def perimeter_calcuation(self):#Создаем метод для расчета периметра
        p = 2 * (self.length + self.width)#Вычисляем периметр прямоугольника по формуле
        return f'P = {p}'#Возвращаем значение периметра прямоугольника

    def square_calcuation(self): #Создаем метод для расчета площади
        s = self.length * self.width#Вычисляем площадь  прямоугольника по формуле
        return f'S = {s}'#Возвращаем значение площади прямоугольника

rectangle_1 = Rectangle(10,5)
p = rectangle_1.perimeter_calcuation()
s = rectangle_1.square_calcuation()
print(p, f'P = ({rectangle_1.length} + {rectangle_1.width}) * 2')
print(s, f'S = {rectangle_1.length} * {rectangle_1.width}')