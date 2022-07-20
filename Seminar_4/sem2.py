# n= int(input('Введите число: '))

# with open('test.txt','w') as file:
#     for i in range(n+1):
#         file.writelines("%s\n" % i)

# a=[]
# with open('test.txt','r') as file:
#     for line in file:
#         a.append(int(line.rstrip()))
# print(a)

# read_file = file.read()
# list_of_rows = read_file.split()

import math
d= 0.001

print('{0:.4}'.format(math.pi))

exit()

# 2. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

list=[]
with open('test.txt','r') as file:
    list_of_rows = file.read().split()
    for item in list_of_rows:
        list.append(int(item))
print(list)

for i in range(len(list)):
    if i==0:
        continue
    elif (list[i]-1) == list[i-1]:
        print(i)

# list[i]-1 == list[i-1]

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов 
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:

# Иванов 23543.12
# Петров 13749.32

