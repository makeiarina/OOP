class Library:# Создаем класс Library
    def __init__(self, name, department):# Создаем метод init
        self.name = name# Инициируем переменную name
        self.department = department# Инициируем переменную department
        self.genre = None# Устанавливаем переменную genre в None
        self.num_editions = 0# Устанавливаем переменную numeditions в 0

class Publication:# Создаем класс Publication
    def __init__(self, title, author, year):# Создаем метод init
        self.title = title# Инициируем переменную title
        self.author = author# Инициируем переменную author
        self.year = year # Инициируем переменную year

    def generate_description(self):# Создаем метод generate_description
        try:
            if self.title is None or self.title == '':# Проверяем, что значение переменной title не является None или пустым
                raise ValueError('Title cannot be empty')# Выбрасываем исключение с сообщением об ошибке
            if self.author is None or self.author == '':# Проверяем, что значение переменной author не является None или пустым
                raise ValueError('Author cannot be empty')# Выбрасываем исключение с сообщением об ошибке
            return f'{self.title} by {self.author}, published in {self.year}'# Возвращаем описание публикации
        except ValueError as e:
            print(f'Error: {e}')# Выводим сообщение об ошибке

class Book(Publication):# Создаем класс Book на основе класса Publication
    def __init__(self, title, author, year, summary):# Создаем метод init
        super().__init__(title, author, year)# Вызываем метод init класса Publication
        self.summary = summary# Инициируем переменную summary

    def generate_description(self):# Создаем метод generate_description
        try:
            super().generate_description()# Вызываем метод generatedescription класса Publication
            if self.summary is None or self.summary == '':# Проверяем, что значение переменной summary не является None или пустым
                raise ValueError('Summary cannot be empty')# Выбрасываем исключение с сообщением об ошибке
            return f'{super().generate_description()} - {self.summary}'# Возвращаем описание книги
        except ValueError as e:
            print(f'Error: {e}')# Выводим сообщение об ошибке

class Magazine(Publication):# Создаем класс Magazine на основе класса Publication
    def __init__(self, title, author, year, articles):# Создаем метод init
        super().__init__(title, author, year)# Вызываем метод init класса Publication
        self.articles = articles# Инициируем переменную articles

    def generate_description(self):# Создаем метод generate_description
        try:
            super().generate_description()# Вызываем метод generate_description класса Publication
            if self.articles is None or self.articles == '':# Проверяем, что значение переменной articles не является None или пустым
                raise ValueError('Articles cannot be empty') # Выбрасываем исключение с сообщением об ошибке
            return f'{super().generate_description()} - {self.articles}'# Возвращаем описание журнала
        except ValueError as e:
            print(f'Error: {e}')# Выводим сообщение об ошибке
library = Library('Библиотека имени Пушкина', 'Классика')# Создаем экземпляр класса Library
book = Book('Евгений Онегин', 'А.С. Пушкин', 1833, 'Роман в стихах')# Создаем экземпляр класса Book
magazine = Magazine('Наука и жизнь', 'Редакция журнала', 2023, 'Статьи о науке и технологиях')# Создаем экземпляр класса Magazine

print(book.generate_description())# Выводим описание книги
print(magazine.generate_description())# Выводим описание журнала