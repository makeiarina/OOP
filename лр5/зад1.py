class C:#Эта строка начинает определение нового класса под названием C.
    def __init__(self, a, b=5):#Создаем конструктор класса C с аргументами a и b
        self.a = a#Эта строка присваивает значение параметра a, переданного конструктору класса, экземпляру переменной a объекта.
        self.b = b#Эта строка присваивает значение параметра b (или значение по умолчанию 5, если значение не было предоставлено) переданному конструктору класса экземпляру переменной b объекта.
    def c(self):#Создаем метод c без аргументов
        return self.a + self.b#Возвращаем сумму a и b
    def d(self): #Создаем метод d без аргументов
        return self.a - self.b#Возвращаем вычитания a и b

a1 = C(5)#Содание объекта C с значением 5
print(f'{a1.a} + {a1.b} =', a1.c())#Выводим на экран сумму
a2 = C(4, 6)#Создание объекта C c значениями a=4,b=6
print(f'{a2.a} - {a2.b} =', a2.d())#Выводим на экран разность