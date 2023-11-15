class Phone:
    '''Класс, представляющий модель абонента.'''

    def init(self, last_name, first_name, middle_name, address, number, time_of_intra_city_conversations,
             time_of_long_distance_conversations):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.number = number
        self.time_of_intra_city_conversations = time_of_intra_city_conversations
        self.time_of_long_distance_conversations = time_of_long_distance_conversations

    # Определяется метод для инициализации объекта класса `Phone`.

    def print_info(self):
        '''Метод для вывода информации об абоненте.'''
        print(f'ФИО: {self.last_name} {self.first_name} {self.middle_name}')
        print(f'Адрес: {self.address}')
        print(f'Номер: {self.number}')
        print(f'Время внутригородних разговоров: {self.time_of_intra_city_conversations}')
        print(f'Время междугородних разговоров: {self.time_of_long_distance_conversations}')
    # Определяется метод для вывода информации об абоненте, использующий атрибуты объекта класса `Phone`.

