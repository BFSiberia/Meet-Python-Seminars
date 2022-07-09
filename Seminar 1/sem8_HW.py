# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
q = 0


def PrintCoordinats(x, y, q):
    print(f'Точка с координатами x = {x}; y = {y} -> {q} четверть')


if x > 0 and y > 0:
    PrintCoordinats(x,y,q=1)
elif x < 0 and y < 0:
    PrintCoordinats(x,y,q=3)
elif x > 0 and y < 0:
    PrintCoordinats(x,y,q=2)
else:
    PrintCoordinats(x,y,q=3)
