# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16]
#         - [2, 3, 5, 6] => [12, 15]

from audioop import reverse
import random

n = abs(int(input('Задайте количество элементов списка: ')))
l_base = [random.randint(1,21) for i in range(n)]

t = map(lambda i: [l_base[i],l_base[n-1-i]], range(int(len(l_base)/2+0.5)))

l_mult =list(map(lambda i:i[0]*i[1], t))

print(f'Произведения пар чисел списка {l_base} => {l_mult}')

# Первый вариант
# l_mult=[l_base[i]*l_base[n-1-i] for i in range(int(len(l_base)/2+0.5))]