# проверить число на простоту (т.е. что число делится только на 1 и само на себя)

def CheckPrime(n):
    if n < 2:
        print('Число должно быть больше 1.')
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    else:
        return True

print(CheckPrime(int(input('Введите число: '))))
