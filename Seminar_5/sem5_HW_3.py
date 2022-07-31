# Создайте программу для игры в ""Крестики-нолики"".

def PGprint(playground):
    for i in range(3):
            print("|", playground[0+i*3],"|",playground[1+i*3],"|",playground[2+i*3],"|")
            print()

def get_player(dict, value): # Поиск ключа по значению
    for i in dict.keys():
        if dict[i] == value:
            return(i)

def nextturn(sign):
    correct = False
    while not correct:
        turn=int(input(f'{get_player(sides, sign)}, ваш ход: '))
        if turn >=1 and turn <=9:
            if (str(playground[turn-1]) not in sides.values()):
                playground[turn-1] = sign
                correct = True
            else:
                print(cites['ocupied'])
        else:
            print(cites['incorrect'])
    playground[turn-1]=sign

def wincheck(playground):
    win_options = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win_options:
        if playground[i[0]] == playground[i[1]] == playground[i[2]]:
            return get_player(sides, sign)
    return False

playground = [1,2,3,4,5,6,7,8,9] # Поле игры

sides=\
    {
        'Игрок 1': 'x',
        'Игрок 2': 'o'
    }

cites=\
    {
        'intro':'Игра в "Крестики-нолики',
        'start': 'Чтобы сделать ход, введите номер клетки.',
        'ocupied': 'Эта клетка занята.',
        'incorrect': 'Ошибка. Введите число от 1 до 9.',
        'win': 'Поздравляем, {}, вы выиграли!',
        'duce': 'Ничья! Спасибо за игру.'
    }

p=1 # Игрок
t=0 # Ход
win=False

print(cites['intro'])
print(cites['start'])

while not win:
    t+=1
    print(f'Ход {t}')
    PGprint(playground)
    if p==1:
        sign=sides['Игрок 1']
    else:
        sign=sides['Игрок 2']
    
    nextturn(sign)
    p*=-1

    if t > 4:
        if wincheck(playground):
            print(cites['win'].format(get_player(sides, sign)))
            win = True
            break
        if t == 9:
            print(cites['duce'])
            break