class Vector:#  В коде определен класс с названием "Vector" (вектор)
  def __init__(self, *args):#В классе "Vector" определен метод инициализации (init), который принимает произвольное количество аргументов (*args
    self.values=[]# Внутри метода инициализации создается пустой список "values"
    for n in args:#В цикле проходится по всем аргументам, переданным при создании объекта класса Vector
      if isinstance(n, (int, float)):# Если текущий аргумент является типом int или float, то он добавляется в список "values"
        self.values.append(n)
  def __str__(self):# Метод "str" определен для класса Vector
    if self.values:# Если список "values" не пустой, то метод "str" возвращает строку вида "Вектор (значения в отсортированном порядке)"
      return f'Вектор{tuple(sorted(self.values))}'
    else:#  Иначе, если список "values" пустой, то метод "str" возвращает строку "Пустой вектор"
      return f'Пустой вектор'
v1 = Vector(1, 2, 3)# В коде создается объект Vector с аргументами 1, 2, 3
print(v1)
v2 = Vector()# В коде создается объект Vector без передачи аргументов
print(v2)