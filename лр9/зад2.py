#Определение класса Book с атрибутами author, title и year. Метод __init__ инициализирует объект класса Book с тремя аргументами author, title и year и устанавливает соответствующие атрибуты.
class Book:
    # Метод init инициализирует объект класса Book с тремя аргументами: author, title и year, и устанавливает соответствующие атрибуты объекта
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def get_info(self):# Метод get_info возвращает информацию о книге в виде строки
        return f"Книга: {self.title}\nАвтор: {self.author}\nГод выпуска: {self.year}"


class Magazine:# Определение класса Magazine, который представляет журнал
    def __init__(self, title, number, year):# Метод init инициализирует объект класса Magazine с тремя аргументами: title, number и year,
    # и устанавливает соответствующие атрибуты объекта
        self.title = title
        self.number = number
        self.year = year

    def get_info(self):# Метод get_info возвращает информацию о журнале в виде строки
        return f"Журнал: {self.title}\nНомер: {self.number}\nГод выпуска: {self.year}"  # включая название, номер и год выпуска

book = Book("Иванов Иван", "Война и мир", 1869)# Создание объекта класса Book с аргументами "Иванов Иван", "Война и мир", 1869
magazine = Magazine("National Geographic", 3, 2022)# Создание объекта класса Magazine с аргументами "National Geographic", 3, 2022

# Полиморфный вызов метода get_info()
print(book.get_info())
print()
print(magazine.get_info())