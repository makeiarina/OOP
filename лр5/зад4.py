class Counter:#класс Counter создает объект, представляющий счетчик
    def __init__(self):
        self.value = 0#в конструкторе класса инициализируется атрибут value, который будет хранить текущее значение счетчика

    def start_from(self, start_value=0):#метод start_from позволяет установить начальное значение счетчика
        self.value = start_value#

    def increment(self):#метод increment увеличивает значение счетчика на
        self.value += 1

    def display(self):#метод display выводит текущее значение счетчика на экран
        print("Текущее значение счетчика =", self.value)

    def reset(self):#метод reset сбрасывает значение счетчика на 0
        self.value = 0

c1 = Counter()#создается объект c1 класса Counte
c1.start_from()#затем вызывается метод start_from без аргументов, что приводит к установке начального значения счетчика в 0
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 1"
c1.increment()#вызывается метод increment для увеличения значения счетчика на 1
c1.display()  # печатает "Текущее значение счетчика = 2"
c1.reset()#вызывается метод reset, который сбрасывает значение счетчика на 0
c1.display()  # печатает "Текущее значение счетчика = 0"

c2 = Counter()#создается новый объект c2 класса Counter
c2.start_from(3)#затем вызывается метод start_from с аргументом 3, что приводит к установке начального значения счетчика в 3
c2.display()  # печатает "Текущее значение счетчика = 3"
c2.increment()#вызывается метод increment для увеличения значения счетчика на 1
c2.display()  # печатает "Текущее значение счетчика = 4"