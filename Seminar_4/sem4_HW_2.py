# Составить список простых множителей натурального числа N

def FactList(n):
    def prime_check(n):
        if n in [2,3]:
            return True
        if n%2==0 or n<2:
            return False
        for i in range(3, n//2+1, 2):
            if n%i==0:
                return False
        return True 
    l1= [i for i in range(2,n//2 + 1) if n%i==0 and prime_check(i)]
    return l1

n = int(input('Введите натуральное число: '))
print('Список простых множителей числа {}: {}'.format(n,FactList(n)))