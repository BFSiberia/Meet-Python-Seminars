# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def MultiLine(n):
    print('Набор произведений от 1 до N')
    result =1
    for i in range(1,n+1):
        result *=i
        print(result, end=' ')

n=int(input('Введите число N: '))

MultiLine(n)