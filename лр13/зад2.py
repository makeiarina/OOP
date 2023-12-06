from tkinter import *#импортирует все классы и функции из модуля tkinter

def clicked():# определяет функцию clicked(), которая будет вызываться при нажатии на кнопку “Приветствие”
    lab.configure(text='Первые успехи')# устанавливает текст Label на экране
def close_window():#определяет функцию close_window(), которая будет вызываться при закрытии окна
    window.destroy()

window=Tk()#создает главное окно приложения
window.title('Проект 2')#устанавливает заголовок главного окна
window.geometry('400x100')#устанавливает размеры главного окна

lab=Label(window,text="",font=('Arial',14),bg='lightyellow')#создает Label с пустым текстом и устанавливает шрифт Arial размером 14
lab.grid(column=1,row=0)#размещает Label в главном окне в первом столбце и первой строке

btn=Button(window,text='Приветствие',font=('Arial',14),command=clicked, bg='lightgreen')#создает Button с текстом “Приветствие” и устанавливает шрифт Arial размером 14. При нажатии на кнопку будет вызываться функция clicked()
btn.grid(column=0, row=1)#размещает Button в главном окне в первом столбце и второй строке

btn1=Button(window,text='Закрыть',font=('Arial',14),command=close_window, bg='lightcoral')#создает Button с текстом “Закрыть” и устанавливает шрифт Arial размером 14. При нажатии на кнопку будет вызываться функция close_window()
btn1.grid(column=2,row=1)#размещает Button в главном окне в третьем столбце и второй строке

window.mainloop()#запускает главный цикл приложения, который обрабатывает события и отображает графический интерфейс