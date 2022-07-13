# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

def Sum4Expression(n):
    global sum
    s = [0]*n
    sum=0
    for i in range(len(s)):
        s[i]=round((1+1/(i+1))**(i+1),4)
        sum+=s[i]
    return s


n = abs(int(input('Задайте число N: ')))

print('Cумма чисел последовательности (1+1/n)**n для числа {0} равна {2}'.format(n, Sum4Expression(n), sum))

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