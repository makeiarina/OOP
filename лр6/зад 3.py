class Phone:
    '''Класс, представляющий модель абонента.'''

    def __init__(self, last_name, first_name, middle_name, address, number, time_of_intra_city_conversations,
                 time_of_long_distance_conversations):
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


def peoplewhohaveusedlongdistancecommunication(persons):
    '''Функция, которая получает список объектов класса Phone и возвращает список объектов,
    воспользовавшихся междугородними разговорами.'''

    p_list = []

    for person in persons:
        if person.time_of_long_distance_conversations > 0:
            p_list.append(person)

    return p_list


phones = [
    Phone('Маникало', 'Полина', 'Александровна', 'Мосты', '+375259555898', '5 часов', 0.1),
    Phone('Белуш', 'Дарья', 'Руслановна', 'Дятлово', '+375259824780', '8 часов', 0),
    Phone('Макей', 'Арина', 'Александровна', 'Островец', '+375297306409', '3 часа', 0),
    Phone('Капыш', 'Вероника', 'Александровна', 'Сморгонь', '+375336161928', '7 часов', 0),
    Phone('Казойть', 'Кирилл', 'Геннадьевич', 'Сморгонь', '+375445934282', '4 часа', 3)
]

long_distance_users = peoplewhohaveusedlongdistancecommunication(phones)

for user in long_distance_users:
    user.print_info()
    print()