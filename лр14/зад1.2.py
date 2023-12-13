from tkinter import *  # Импортируем модуль для создания графического интерфейса
from tkinter import ttk

def getInfo():  # Создаем метод для вывода информации
    file = open('info.txt', 'w', encoding='utf-8')  # Открываем файл для записи
    file.write('Имя: ' + nameT.get() + '\n')  # Записываем в файл информацию из nameT
    file.write('Фамилия: ' + lastNameT.get() + '\n')  # Записываем в файл информацию из lastNameT
    if polvar.get() == 'm':
        file.write('Пол: мужской\n')
    elif polvar.get() == 'w':
        file.write('Пол: женский\n')
    else:
        file.write('Пол не указан\n')
    file.write('Любимые предметы:\n')  # В зависимости от выбора флажков, записываем информацию о предметах
    if var1.get() == 1:
        file.write(' - математика\n')
    if var2.get() == 1:
        file.write(' - английский язык\n')
    if var3.get() == 1:
        file.write(' - информационные технологии\n')
    file.close()

window = Tk()  # Создаем окно
window.title('Регистрация')  # Устанавливаем название окна

name = Label(window, text='Имя', width=20, height=1, fg='blue', font='arial 18')  # Создаем метки
lastName = Label(window, text='Фамилия', width=20, height=1, fg='blue', font='arial 18')
pol = Label(window, text='Пол', width=20, height=1, fg='blue', font='arial 18')
likePr = Label(window, text='Любимые предметы', width=20, height=1, fg='blue', font='arial 18')

nameT = Entry(window, width=30, font='arial 14')  # Создаем поля для ввода

lastNameT = Entry(window, width=30, font='arial 14')

polvar = StringVar()  # Создаем переменную для группы переключателей
polvar.set(' ')
radio1 = Radiobutton(window, text='мужской', variable=polvar, value='m')  # Создаем переключатели
radio2 = Radiobutton(window, text='женский', variable=polvar, value='w')

var1 = IntVar()  # Создаем переменные для флажков
var2 = IntVar()
var3 = IntVar()
check1 = Checkbutton(window, text='математика', variable=var1, onvalue=1, offvalue=0)  # Создаем флажки
check2 = Checkbutton(window, text='английский язык', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(window, text='информационные технологии', variable=var3, onvalue=1, offvalue=0)

btn = Button(window, text='Принять', width=25, height=5, fg='blue', font='arial 14', command=getInfo)  # Создаем кнопку для вывода информации

# Устанавливаем расположение всех элементов с помощью метода pack()
name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()

window.mainloop()  # Запускаем цикл обработки событий для отображения окна и взаимодействия с пользователем