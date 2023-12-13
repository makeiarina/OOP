from tkinter import *  # Импортируем все классы и функции модуля tkinter
from tkinter import ttk

def getInfo():  # Определяем функцию для вывода информации
    print('Имя: ', nameT.get())  # Выводим информацию об имени
    print('Фамилия: ', lastNameT.get())  # Выводим информацию о фамилии
    if polvar.get() == 'm':  # Проверяем выбранный пол
        print('Пол: мужской')  # Выводим информацию о мужском поле
    elif polvar.get() == 'w':  # Проверяем выбранный пол
        print('Пол: женский')  # Выводим информацию о женском поле
    else:
        print('Пол не указан')  # Выводим информацию, если пол не выбран
    print('Любимые предметы: ')
    if var1.get() == 1:  # Проверяем, выбран ли первый предмет
        print(' - математика')  # Выводим информацию о предмете
    if var2.get() == 1:  # Проверяем, выбран ли второй предмет
        print(' - английский язык')  # Выводим информацию о предмете
    if var3.get() == 1:  # Проверяем, выбран ли третий предмет
        print(' - информационные технологии')  # Выводим информацию о предмете

window = Tk()  # Создаем новое окно
window.title('Регистрация')  # Устанавливаем заголовок окна

name = Label(window, text='Имя', width=20, height=1, fg='blue', font='arial 18')  # Создаем надпись "Имя"
lastName = Label(window, text='Фамилия', width=20, height=1, fg='blue', font='arial 18')  # Создаем надпись "Фамилия"
pol = Label(window, text='Пол', width=20, height=1, fg='blue', font='arial 18')  # Создаем надпись "Пол"
likePr = Label(window, text='Любимые предметы', width=20, height=1, fg='blue', font='arial 18')  # Создаем надпись "Любимые предметы"

nameT = Entry(window, width=30, font='arial 14')  # Создаем поле ввода для имени
lastNameT = Entry(window, width=30, font='arial 14')  # Создаем поле ввода для фамилии

polvar = StringVar()  # Создаем строковую переменную для группы переключателей
polvar.set(' ')  # Устанавливаем начальное значение

radio1 = Radiobutton(window, text='мужской', variable=polvar, value='m')  # Создаем переключатель для мужского пола
radio2 = Radiobutton(window, text='женский', variable=polvar, value='w')  # Создаем переключатель для женского пола

var1 = IntVar()  # Создаем целочисленную переменную для группы флажков
var2 = IntVar()
var3 = IntVar()

check1 = Checkbutton(window, text='математика', variable=var1, onvalue=1, offvalue=0)  # Создаем флажок для предмета "математика"
check2 = Checkbutton(window, text='английский язык', variable=var2, onvalue=1, offvalue=0)  # Создаем флажок для предмета "английский язык"
check3 = Checkbutton(window, text='информационные технологии', variable=var3, onvalue=1, offvalue=0)  # Создаем флажок для предмета "информационные технологии"

btn = Button(window, text='Принять', width=25, height=5, fg='blue', font='arial 14', command=getInfo)  # Создаем кнопку "Принять"

name.pack()  # Располагаем надпись "Имя" на форме
nameT.pack()  # Располагаем поле для ввода имени на форме
lastName.pack()  # Располагаем надпись "Фамилия" на форме
lastNameT.pack()  # Располагаем поле для ввода фамилии на форме
pol.pack()  # Располагаем надпись "Пол" на форме
radio1.pack()  # Располагаем переключатель "мужской" на форме
radio2.pack()  # Располагаем переключатель "женский" на форме
likePr.pack()  # Располагаем надпись "Любимые предметы" на форме
check1.pack()  # Располагаем флажок "математика" на форме
check2.pack()  # Располагаем флажок "английский язык" на форме
check3.pack()  # Располагаем флажок "информационные технологии" на форме
btn.pack()  # Располагаем кнопку "Принять" на форме

window.mainloop()  # Вызываем цикл обработки событий для отображения окна и взаимодействия с пользователем