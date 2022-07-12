# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} (не корректный)

def Sum4Expression(n):
    s = [0]*n
    for i in range(len(s)):
        s[i]=round((1+1/(i+1))**(i+1)+s[i-1],4)
    return s


n = int(input('Задайте число N: '))

print('Список сумм последовательности числа {}: {}'.format(n, Sum4Expression(n)))

# Первый вариант через добавление нового элемента списка с переменной итогов суммирования

# def Sum4Expression(n):
#     s = []
#     sum = 0
#     for i in range(1,n+1):
#         sum += round((1+1/i)**i,4)
#         s.append(sum)
#     return s


# n = int(input('Задайте число N: '))

# print('Список сумм последовательности числа {}: {}'.format(n, Sum4Expression(n)))