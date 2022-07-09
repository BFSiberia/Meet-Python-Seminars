# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным

day_of_week = ['понедельник', 'вторник', 'среда',
               'четверг', 'пятница', 'суббота', 'воскресенье']

d = int(input('Введите номер дня недели: '))

if d not in range(1, 8):
    print('Такого дня недели не существует.')
elif d > 5:
    print(f'{day_of_week[d-1]} - это выходной')
else:
    print(f'{day_of_week[d-1]} - это не выходной')
