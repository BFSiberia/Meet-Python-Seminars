# Создайте программу для игры в ""Крестики-нолики"".

def Playprint(list):
    for row in list:
        for elem in row:
            print(str(elem), end = ' ')
        print()

sides=\
    {
        'Игрок 1': 'x',
        'Игрок 2': 'o'
    }

cites=\
    {
        'intro':'Игра в "Крестики-нолики',
        'start': 'Чтобы сделать ход, введите координаты клетки через пробел,\nнапример: 1 1 - для верхнего левого угла, 2 2 - для центра'
    }

p=1 # Игрок
t=0 # Ход
playground = [[0,1,2,3],[1,'','',''],[2,'','',''],[3,'','','']] # Поле игры

print(cites['intro'])
print(cites['start'])

if p==1:
    sign=sides['Игрок 1']
else:
    sign=sides['Игрок 2']
   
turn=(input(f'Игрок № {p}, ваш ход: '))
coords=turn.split()
playground[int(coords[0])][int(coords[1])]=sign
Playprint(playground)

