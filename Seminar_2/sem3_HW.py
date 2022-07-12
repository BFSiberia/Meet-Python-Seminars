# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def NumberSum(number):
    number = abs(number)
    if number % 1 > 0:
        s1 = str(number)
        s1 = s1.replace('.', '')
        number = int(s1)*10

    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return int(sum)


x = float(input('Введите любое вещественное число: '))

print('Сумма цифр числа {} равна {}'.format(x,NumberSum(x)))