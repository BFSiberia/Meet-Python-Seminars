# Вывести на экран числа от -N до N

import math


N = abs(int(input(f'Введите число N: ')))
a = range(-N, N+1)

for i in a:
    print(i)