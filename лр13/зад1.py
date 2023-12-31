from tkinter import *#Эта строка импортирует все классы и функции из модуля tkinter, который предоставляет инструменты для создания графического пользовательского интерфейса.
#В этой строке определена функция close_window(), которая будет вызываться при нажатии на кнопку. Она вызывает метод destroy() объекта window, что приводит к закрытию окна.
def close_window():
    window.destroy()
window = Tk()#Эта строка создает объект window класса Tk, который представляет собой главное окно приложения
window.title('Проект 1')#В этой строке задается заголовок (title) для главного окна приложения. Здесь заголовок установлен как "Проект 1"
window.geometry('400x100')#Строка задает размер (geometry) главного окна. Здесь установлен размер 400 пикселей по ширине и 100 пикселей по высоте
#В этом блоке создается объект класса Label (метка), который будет отображаться в главном окне. Метка имеет текст "Моя первая программа" и шрифт Arial размером 14 пунктов. Метод pack() вызывается для расположения метки в главном окне
lab = Label(window, text='Моя первая программа', font=('Arial',14),fg='Purple')
lab.pack()
#Этот блок создает объект класса Button (кнопка), который будет отображаться в главном окне. Кнопка имеет текст "Закрыть", шрифт Arial размером 14 пунктов и атрибут command, который связывает кнопку с функцией close_window(). Метод pack() вызывается для расположения кнопки в главном окне
btn = Button(window, text = 'Закрыть', font=('Arial', 14), command = close_window,bg='Purple',fg='White')
btn.pack()
#Эта строка запускает бесконечный цикл (mainloop()), который отображает главное окно и обрабатывает события, пока окно не будет закрыто
window.mainloop()