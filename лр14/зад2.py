from tkinter import *#С помощью этого модуля создаем графический интерфейс
window = Tk()#Создаем окно
window.geometry("250x200")#Задаем размеры для окна
list1 = Listbox(window, height = 5, width = 15, selectmode = EXTENDED)#Создаем список(можно выбрать несколько пунктов)
list2 = Listbox(window, height = 5, width = 15, selectmode = SINGLE)#Создаем список(можно выбрать только один пункт
lst1 = ['Минск', 'Молодечно', 'Борисов', 'Мозырь', 'Воложин']#Создаем список и задаем содержимое
lst2 = ['Гродно', 'Ивье', 'Новогрудок', 'Ошмяны', 'Островец']
for i in lst1:#Добавляем элементы из lst1 в list1
    list1.insert(END, i)
for i in lst2:#Добавляем элементы из lst2 в list2
    list2.insert(END, i)
list1.pack()#Располагаем списки посередине
list2.pack()
window.mainloop()#Цикл обработки событий для отображения окна и взаимодействия с пользователем