class Vector:
    def __init__(self,*args): # конструктор получает произвольное количество аргументов
        self.values = []
        for arg in args:
            if isinstance(arg,int): # проверяем, является ли аргумент целым числом
                self.values.append(arg)# добавляем аргумент в список значений
            self.values.sort()# сортируем значения в порядке возрастания
    def __str__(self):
        if len(self.values) == 0:# если список значений пустой
            return 'пусть вектор'# возвращаем строку "пусть вектор"
        return f'вектор{tuple(self.values)}'# возвращаем строку "вектор" и кортеж значений
    def __add__(self, other):
        new_v=[]
        if isinstance(other, Vector): # если other является объектом типа Vector
            if len(self.values) == len(other.values): # если длины векторов равны
                for i in range(len(self.values)):
                    new_v.append(self.values[i] + other.values[i])# добавляем сумму соответствующих значений в новый список
                return Vector(*[i for i in new_v])# создаем новый объект Vector с новым списком значений
            else:#иначе
                print('сложение векторов разной длины недопустимо.')# выводим сообщение об ошибке, если длины векторов разные
        if isinstance(other, int): # если other является целым числом
            for i in range(len(self.values)):
                new_v.append(self.values[i]+other)# добавляем сумму каждого значения с other в новый список
            return Vector(*[i for i in new_v]) # создаем новый объект Vector с новым списком значений
            if not isinstance(other, (Vector, int)):# если other не является ни объектом типа Vector, ни целым числом
                print(f'Вектор нельзя сложить с {other}')# выводим сообщение об ошибке

    def __mul__(self, other):
        new_v = []
        if isinstance(other, Vector): # если other является объектом типа Vector
            if len(self.values) == len(other.values):# если длины векторов равны
                for i in range(len(self.values)):
                    new_v.append(self.values[i] * other.values[i])# добавляем произведение соответствующих значений в новый список
                return Vector(*[i for i in new_v])# создаем новый объект Vector с новым списком значений
            else:#иначе
                print('сложение векторов разной длины недопустимо.')# выводим сообщение об ошибке, если длины векторов разные
        if isinstance(other, int):# если other является целым числом
            for i in range(len(self.values)):
                new_v.append(self.values[i] * other) # добавляем произведение каждого значения на other в новый список
            return Vector(*[i for i in new_v])# создаем новый объект Vector с новым списком значений
            if not isinstance(other, (Vector, int)): # если other не является ни объектом типа Vector, ни целым числом
                print(f'Вектор нельзя сложить с {other}')# выводим сообщение об ошибке
v1=Vector(1,2,3)
print(v1)
v2=Vector(4,7,1,12)
print(v2)
print(v1+v2)
v3=Vector(7,11,3,18)
print(v2+v3)
v4=Vector(4,6,8)
v5=Vector(5,3,2)
print(v4*v5)
