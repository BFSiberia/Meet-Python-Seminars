# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def fac(n):
 if n in [1]:
    return 1
 else:
    return n * fac(n-1)

n=int(input('Введите число N: '))

list = []

for e in range(1, n+1):
    list.append(fac(e))

print(f'Список произведений от 1 до {n}: {list}')

# Пробы пера до того, как вышла вторая лекция

# def MultiLine(n):
#     print('Список произведений от 1 до N')
#     result =1
#     for i in range(1,n+1):
#         result *=i
#         print(result, end=' ')

# n=int(input('Введите число N: '))

# MultiLine(n)

# def MultiLine(n):
#     s=[0]*n
#     for i in range(1,len(s)):
#         s[0]=1
#         s[i]=(i+1)*s[i-1]
#     return s

# n=int(input('Введите число N: '))

# print(f'Список произведений от 1 до {n}: {MultiLine(n)}')