# найти факториал числа

from tkinter import N


def Fact(n):
    if n in range(2):
        return 1
    else:
        return n*Fact(n-1)

n = int(input('Введите число: '))

print(f'Факториал числа {n} равен {Fact(n)}')
