# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random as rnd

# Создам файлы с коэфициентами
with open ('poly1.txt', 'w') as p1:
    p1.writelines('%s ' % rnd.randint(-20,20) for i in range(4))

with open ('poly2.txt', 'w') as p2:
    p2.writelines('%s ' % rnd.randint(-20,20) for i in range(4))

# Суммируем многочлены
with open ('poly1.txt', 'r') as p1: 
    r1 =p1.read().split()

with open ('poly2.txt', 'r') as p2: 
    r2 =p2.read().split()

with open ('polyresult.txt' , 'w') as pr:
    pr.writelines('%s ' % i for i in map(lambda x,y: x+y, map(int,r1),map(int,r2)))