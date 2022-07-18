# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibo(n-2)+Fibo(n-1)


def NegFibo(n):
    n *= -1
    if -n > -1:
        return 0
    elif -n > -2:
        return 1
    else:
        return NegFibo(-n+2)-NegFibo(-n+1)


number = abs(int(input('Введите целое положительное число: ')))

list_fibo = [Fibo(i) for i in range(1, number+1)]

list_negfibo = [NegFibo(i) for i in range(-number, 1)]

combined_list = [list_negfibo, list_fibo]
list_merge = [i for sublist in combined_list for i in sublist]

print(list_merge)
