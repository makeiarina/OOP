class Phone:
    '''Класс, представляющий модель абонента.'''

    def __init__(self, last_name, first_name, middle_name, address, number, time_of_intra_city_conversations,
             time_of_long_distance_conversations):
        '''
        Метод для инициализации объекта класса Phone.

        Параметры:
        last_name (str): Фамилия абонента.
        first_name (str): Имя абонента.
        middle_name (str): Отчество абонента.
        address (str): Адрес абонента.
        number (str): Номер телефона абонента.
        time_of_intra_city_conversations (str): Время внутригородних разговоров абонента.
        time_of_long_distance_conversations (str): Время междугородних разговоров абонента.
        '''
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.number = number
        self.time_of_intra_city_conversations = time_of_intra_city_conversations
        self.time_of_long_distance_conversations = time_of_long_distance_conversations

    def print_info(self):
        '''Метод для вывода информации об абоненте.'''
        print(f'ФИО: {self.last_name} {self.first_name} {self.middle_name}')
        print(f'Адрес: {self.address}')
        print(f'Номер: {self.number}')
        print(f'Время внутригородних разговоров: {self.time_of_intra_city_conversations}')
        print(f'Время междугородних разговоров: {self.time_of_long_distance_conversations}')
        '''Метод для вывода информации об абоненте, использующий атрибуты объекта класса Phone.'''

