# найти наибольший простой делитель числа

def CheckPrime(n):
    if n < 2:
        print('Число должно быть больше 1.')
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    else:
        return True


def Search(n):
    if CheckPrime(n):
        return print(f'{n}- простое число')

    max = 0
    for i in range(2, n):
        if n % i == 0 and CheckPrime(i) and i>max:
            max=i
    return print(f'Наибольший простой делитель числа {n} - {max}')

Search(4)