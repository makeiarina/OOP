from зад3 import Phone

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