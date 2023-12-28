# Определение класса Flower
class Flower:
    # Метод инициализации, инициализирующий атрибуты объекта Flower
    def __init__(self, name, freshness, stem_length):
        # Присваивание значений атрибутам объекта с использованием именованных параметров
        self.__name = name
        self.__freshness = freshness
        self.__stem_length = stem_length

    # Свойство name со встроенным геттером
    @property
    def name(self):
        return self.__name

    # Сеттер для свойства name
    @name.setter
    def name(self, value):
        self.__name = value

    # Свойство freshness со встроенным геттером
    @property
    def freshness(self):
        return self.__freshness

    # Сеттер для свойства freshness
    @freshness.setter
    def freshness(self, value):
        self.__freshness = value

    # Свойство stem_length со встроенным геттером
    @property
    def stem_length(self):
        return self.__stem_length

    # Сеттер для свойства stem_length
    @stem_length.setter
    def stem_length(self, value):
        self.__stem_length = value

    # Метод с магическим методом str, возвращающий строковое представление объекта Flower
    def __str__(self):
        return f"Flower: {self.__name}, Freshness: {self.__freshness}, Stem Length: {self.__stem_length}"

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