# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

list = []

for i in range(6):
    list.append(random.randint(1,10))

result =0
for i, value in enumerate(list):
    if i%2 !=0:
        result+=value

print('Сумма элементов списка {} на нечетных позициях = {}'.format(list,result))