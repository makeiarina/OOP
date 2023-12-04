from tkinter import *
from random import randint
# Определяем функцию roll_dice(), которая будет вызываться при нажатии на кнопку "Бросить кубик"
def roll_dice():
    # Генерируем случайное число от 1 до 6 и выводим его на экран
    label.configure(text=str(randint(1, 6)))
# Определяем функцию close_window(), которая будет вызываться при закрытии окна
def close_window():
    window.destroy()
# Создаем главное окно приложения
window = Tk()
window.title("Брось кубик")
# Создаем Label с текстом "Брось кубик" и устанавливаем шрифт Arial размером 14
label = Label(window, text="Брось кубик", font=("Arial", 14))
label.pack(pady=20)
# Создаем Button с текстом "Бросить кубик" и устанавливаем шрифт Arial размером 14
# При нажатии на кнопку будет вызываться функция roll_dice()
button = Button(window, text="Бросить кубик", font=("Arial", 14), command=roll_dice)
button.pack(pady=10)
# Запускаем главный цикл приложения
window.mainloop()
