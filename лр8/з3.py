class Quadrilateral:
    def __init__(self, width, height=None):#В классе "Quadrilateral" определен метод инициализации (init), который принимает два аргумента - "ширина" и "высота"
        if height is None:  # Если передан только один аргумент
            self.__width = width
            self.__height = width
        else:  # Если передано два аргумента
            self.__width = width
            self.__height = height

    def __str__(self):#В классе определен переопределенный метод "str", который возвращает строковое представление объекта
        if self.__width == self.__height:  # Метод "str" проверяет, если "ширина" и "высота" равны друг другу, и возвращает разные строки для кубов и прямоугольников
            return f"Куб размером {self.__width}x{self.__height}"
        else:
            return f"Прямоугольник размером {self.__width}x{self.__height}"

    def __bool__(self):#определен переопределенный метод "bool", который возвращает True, если объект является квадратом, и False, если объект является прямоугольником
        if self.__width == self.__height:
            print("Это квадрат")
            return True
        else:
            print("Это прямоугольник")
            return False
figura1 = Quadrilateral(7, 7)#В коде создается объект Quadrilateral с шириной и высотой, равными 5
print(figura1.__str__()) # В коде вызывается метод "str" объекта "figura1" и выводится возвращаемая строка
print(figura1.__bool__())#В коде вызывается метод "bool", объекта "figura1", выводится возвращаемое значение и соответствующее сообщение

figura2 = Quadrilateral(7, 10)#В коде создается объект Quadrilateral с шириной 4 и высотой 6
print(figura2.__str__()) # В коде вызывается метод "str" объекта "figura2" и выводится возвращаемая строка
print(figura2.__bool__())# В коде вызывается метод "bool" объекта "figura2", выводится возвращаемое значение и соответствующее сообщение