def data_in():
    dictionry=\
        {
            'Имя': input('Введите ФИО: '),
            'Дата рождения': input('Введите дату рождения: '),
            'Класс': input('Введите класс: '),
            'Место в классе': input('Введите место в классе: '),
            'Статус': input('Введите статус ученика: ')

        }
    with open ('student.txt', 'a', encoding='utf-8') as f:
        f.write(f'{data_in()}\n')

