from tkinter import *#С помощью этого модуля создаем графический интерфейс
from tkinter import ttk#Ипользуем подмодуль


window = Tk()#Создаем окно
window.geometry("300x80")#Задаем размеры окна


value_var = IntVar()#Создаем переменную для хранения значения Progressbar
pb = ttk.Progressbar(window, orient="horizontal", length = 280, variable=value_var, mode = 'determinate')#Создаем Progressbar
pb.pack()#Располагаем его посередине


def start():#Создаем метод для запуска прогресса со скоростью 100
    pb.start(100)
def stop():#Создаем метод для остановки прогресса
    pb.stop()


start_btn = ttk.Button(text="Start", command=start)#Создаем кнопку старта
start_btn.pack()#Располагаем её посередине
stop_btn = ttk.Button(text="Stop", command=stop)#Создаем кнопку стоп
stop_btn.pack()#Располагаем её посередине


window.mainloop()#Цикл обработки событий для отображения окна и взаимодействия с пользователем