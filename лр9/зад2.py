#Определение класса Book с атрибутами author, title и year. Метод __init__ инициализирует объект класса Book с тремя аргументами author, title и year и устанавливает соответствующие атрибуты.
class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def get_info(self):
        return f"Книга: {self.title}\nАвтор: {self.author}\nГод выпуска: {self.year}"


class Magazine:
    def __init__(self, title, number, year):
        self.title = title
        self.number = number
        self.year = year

    def get_info(self):
        return f"Журнал: {self.title}\nНомер: {self.number}\nГод выпуска: {self.year}"

book = Book("Иванов Иван", "Война и мир", 1869)
magazine = Magazine("National Geographic", 2022, 3)

# Полиморфный вызов метода get_info()
print(book.get_info())
print()
print(magazine.get_info())