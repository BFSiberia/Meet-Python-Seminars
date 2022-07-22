# ычислить число pi c заданной точностью d Пример:
# Пример при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

from decimal import Decimal as D
from decimal import getcontext

def Pi_toDigit (d):
    getcontext().prec = d+1
    pi = D(0)
    
    for k in range(10000):
        pi += D(16**-k) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))
    
    return pi

while True:
    d = int(input('Введите количество знаков после запятой Пи от 1 до 10 : '))
    if d > 0 and d <= 10:
        break

print('Число Пи с {} знаками после запятой: {}'.format(d,Pi_toDigit(d)))

# http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula