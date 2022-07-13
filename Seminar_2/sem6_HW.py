# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# 2. Реализуйте алгоритм перемешивания списка.

import random

n = abs(int(input('Введите число N: ')))

s = []

for i in range(-n, n+1):
    s.append(i)
print(f'Список элементов от {-n} до {n}: {s}')

# Создаем файл file.txt с набором из 3x случайных индексов

with open('file.txt', 'w') as f:
    for i in range(3):
        f.write(f'{random.randint(0,len(s)-1)}\n')

# Произведение элементов на позициях из file.txt

f= open('file.txt', 'r')
result=1
for line in f:
    result *= s[int(line)]
print(f'Произведение элементов: {result}')
f.close()

# Перемешивание элементов списка

for i in range(len(s)):
    # Извлечение числа со случайным индексом
    number = s.pop(random.randint(0, len(s)-1))
    # Вставка извлеченного числа на случайное место
    s.insert(random.randint(0, len(s)-1), number)

# random.shuffle(s) встроенный метод перемешивания списка

print('Список элементов от {} до {} после перемешивания: {}'.format(-n, n, s))
