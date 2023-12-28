# Определение класса Flower
class Flower:
    """
    Класс для представления цветка.

    Attributes:
    name (str): Название цветка.
    freshness (int): Уровень свежести цветка.
    stem_length (float): Длина стебля цветка.
    """

    def __init__(self, name, freshness, stem_length):
        """
        Инициализация атрибутов объекта Flower.

        Args:
        name (str): Название цветка.
        freshness (int): Уровень свежести цветка (от 1 до 10).
        stem_length (float): Длина стебля цветка в сантиметрах.
        """
        self.name = name
        self.__freshness = freshness
        self.__stem_length = stem_length

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def freshness(self):
        return self.__freshness

    @freshness.setter
    def freshness(self, value):
        self.__freshness = value

    @property
    def stem_length(self):
        return self.__stem_length

    @stem_length.setter
    def stem_length(self, value):
        self.__stem_length = value

    def __str__(self):
        return f"Flower: {self.__name}, Freshness: {self.__freshness}, Stem Length: {self.__stem_length} cm"


# Создание нескольких экземпляров класса Flower с разными значениями атрибутов
flower1 = Flower("Rose", 8, 10)
flower2 = Flower("Tulip", 6, 12)
flower3 = Flower("Lily", 9, 9)
flower4 = Flower("Sunflower", 7, 15)
flower5 = Flower("Daisy", 5, 11)

# Создание списка, содержащего объекты Flower
flowers = [flower1, flower2, flower3, flower4, flower5]

# Сортировка списка цветов по значению freshness в порядке убывания
sorted_flowers = sorted(flowers, key=lambda x: x.freshness, reverse=True)

# Вывод информации о цветах, отсортированных по уровню свежести
print("Сортировка цветов по уровню свежести:")
for flower in sorted_flowers:
    print(flower)

# Установка минимальной и максимальной длины стеблей для фильтрации цветов
min_stem_length = 10
max_stem_length = 15

# Фильтрация цветов по заданному диапазону длин стеблей
filtered_flowers = [flower for flower in flowers if min_stem_length <= flower.stem_length <= max_stem_length]

# Вывод информации о цветах, отфильтрованных по длине стебля
print("\nЦветы в заданном диапазоне длин стеблей:")
for flower in filtered_flowers:
    print(flower)