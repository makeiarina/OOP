import tkinter as tk#импортирует библиотеку tkinter и дает ей псевдоним tk
from math import sin, sqrt, exp#импортирует функции sin, sqrt и exp из модуля math

def calculate_formula():#определяет функцию calculate_formula()
    x = float(entry.get())# получает значение x из Entry и преобразует его в тип float

    result = sqrt(sin(3*x/2) + pow(sqrt(3), 1.3*x) + pow(exp(-1.3*x), 1.3))#вычисляет значение формулы, используя полученное значение x

    label_result.config(text=f"Результат: {result}")#устанавливает текст Label на экране с результатом вычисления формулы

# Создание графического интерфейса
root = tk.Tk()#создает главное окно приложения
root.title("Подсчет по формуле")#устанавливает заголовок главного окна

# Создание элементов интерфейса
label = tk.Label(root, text="Введите значение x:")#создает Label с текстом “Введите значение x:”
label.pack()#упаковывает Label в главное окно

entry = tk.Entry(root)#создает Entry для ввода значения x
entry.pack()#упаковывает Entry в главное окно

button = tk.Button(root, text="Посчитать", command=calculate_formula)#создает Button с текстом “Посчитать” и связывает его с функцией calculate_formula()
button.pack()# упаковывает Button в главное окно

label_result = tk.Label(root, text="")#создает Label для отображения результата вычисления формулы
label_result.pack()#упаковывает Label в главное окно

# Запуск приложения
root.mainloop()#запускает главный цикл приложения, который обрабатывает события и отображает графический интерфейс