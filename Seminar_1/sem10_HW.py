# Найти расстояние между двумя точками пространства


from math import sqrt
from random import randint


def RndCoordinates(list):
    for i in range(2):
       list.append(randint(-5, 5))
    return list


x = []
RndCoordinates(x)
print(x)
y = []
RndCoordinates(y)
print(y)

distance = sqrt((y[0]-x[0])**2+(y[1]-x[1])**2)
print(f'Растояние между точками: {round(distance,2)}')
