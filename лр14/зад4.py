# импорт всех классов и функций модуля tkinter
from tkinter import *
from tkinter import ttk
import math# импорт модуля для математических операций

# Функция для создания таблицы значений функции
def tabulate_function():
    listbox.delete(0, END)# Очистка списка значений
    step = 1 # Шаг для вычисления значений
    beginning = 1# Начальное значение
    end = 9# Конечное значение
    iterations = int((end - beginning) / step) + 1  # Вычисление количества итераций
    label_function_formula.config(text='y=sin(2x+1)') # Установка текста для метки формулы функции
    listbox.insert(END, '    x         |         y')# Добавление заголовка таблицы
    # Цикл для вычисления значений функции и добавления их в таблицу
    for i in range(iterations):
        x = beginning + i * step# Вычисление значения x
        y = math.sin(2 * x + 1)# Вычисление значения y по формуле функции
        result = f'   {x:.2f}              {y:.2f}'# Форматирование строки с результатом
        listbox.insert(END, result)# Добавление результата в список значений
        progressbar_var.set((i + 1) / iterations * 100)  # Обновление значения прогресс-бара

# Создание окна приложения
wn = Tk()
wn.title('Расчет функции')# Установка заголовка окна
wn.geometry('300x300')# Установка размеров окна

label_function_formula = Label(wn, text='') # Создание метки для отображения формулы функции
label_function_formula.pack()# Размещение метки на форме

tabulate_button = Button(wn, text='Расчет', command=tabulate_function)# Создание кнопки для запуска расчета
tabulate_button.pack()# Размещение кнопки на форме

listbox = Listbox(wn, width=30)# Создание списка для отображения значений функции
listbox.pack() # Размещение списка на форме

progressbar_var = DoubleVar()# Создание переменной для прогресс-бара
progressbar = ttk.Progressbar(wn, variable=progressbar_var, maximum=100)# Создание прогресс-бара
progressbar.pack()# Размещение прогресс-бара на форме

wn.mainloop()# Запуск главного цикла приложения