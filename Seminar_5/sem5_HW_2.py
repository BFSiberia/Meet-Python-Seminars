# Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

import random as rnd

n = 2021  # число конфет
r = range(1, 29)  # Диапазон взятия
p = 1  # первый игрок по умолчанию
# pmode - второй игрок по умолчанию
pcount = [0, 0, 0]  # конфеты у игрока 0,1,2 где 0 - бот
take = 0  # Взято конфет игроком

wording =\
    {
        'pchoice':'Выберите, с кем хотите сыграть:  с человеком - 1, с роботом - 0\nВаш выбор: ',
        'header':'Игра в конфеты.\nВыигрывает тот, кто возьмет конфету последним.',
        'start':'Начинам игру!\n\nКоличество конфет на столе: {}',
        'withdraw':'Игрок № {}, у вас {} конфет. Возьмите от 1 до 28 конфет  со стола: ',
        'bottake':'Робот взял конфет: {}',
        'left':'Осталось конфет: {}',
        'win':'Поздравляем, игрок № {}! Вы победили!'
    }

pmode = int(input(wording['pchoice']))
print(wording['header'],wording['start'].format(n))

while n > 0:
    while True:
        if p == 1:
            take = int(input(wording['withdraw'].format(p, pcount[p])))
            if take in r and n >= take:
                break
        else:
            print(wording['withdraw'].format(p, pcount[p]))
            take = n % (max(r)+1)
            if take == 0:
                take = rnd.randint(1, max(r))
            print(wording['bottake'].format(take))
            break

    pcount[p] += take
    n -= take
    print(wording['left'].format(n))
    if n < 1:
        print(wording['win'].format(p, pcount[p]))
        break
    if p == 1:
        p = pmode
    else:
        p = 1
