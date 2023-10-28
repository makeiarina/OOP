class Flower:# Определяет класс Flower с атрибутами name (имя), freshness (свежесть) и stem_length (длина стебля)
    def __init__(self, name, freshness, stem_length):#Метод __init__ - это конструктор, который инициализирует атрибуты объекта Flower
        self.__name = name
        self.__freshness = freshness
        self.__stem_length = stem_length

    def __str__(self):#Метод __str__ возвращает строковое представление объекта Flower
        return f"Flower: {self.__name}, Freshness: {self.__freshness}, Stem Length: {self.__stem_length}"

    #Определяет методы-геттеры и методы-сеттеры для атрибутов name, freshness и stem_length
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_freshness(self):
        return self.__freshness

    def set_freshness(self, freshness):
        self.__freshness = freshness

    def get_stem_length(self):
        return self.__stem_length

    def set_stem_length(self, stem_length):
        self.__stem_length = stem_length

# Создает несколько экземпляров класса Flower с разными значениями атрибутов
flower1 = Flower("Rose", 8, 10)
flower2 = Flower("Tulip", 6, 12)
flower3 = Flower("Lily", 9, 9)
flower4 = Flower("Sunflower", 7, 15)
flower5 = Flower("Daisy", 5, 11)

# Создает список flowers и добавляет в него объекты Flower
flowers = [flower1, flower2, flower3, flower4, flower5]

# Сортировка цветов по уровню свежести (freshness)
sorted_flowers = sorted(flowers, key=lambda x: x.get_freshness(), reverse=True)

print("Сортировка цветов по уровню свежести:")
for flower in sorted_flowers:
    print(flower)

# Заданный диапазон длин стеблей
min_stem_length = 10#Устанавливает минимальную длину стебля для фильтрации цветов
max_stem_length = 15#Устанавливает максимальную длину стебля для фильтрации цветов

# Найти цветы в заданном диапазоне длин стеблей
filtered_flowers = [flower for flower in flowers if min_stem_length <= flower.get_stem_length() <= max_stem_length]

print("\nЦветы в заданном диапазоне длин стеблей:")
for flower in filtered_flowers:
    print(flower)