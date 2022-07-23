# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 в виде  x^2 + 5*x - 3

from dataclasses import replace
import random as rnd

k = 3

def Polynom (k):
    list =[rnd.randint(0,100) for i in range(rnd.randint(1,4))]
    if len(list)==1:
        draft = ['{}{}*x^{}'.format(rnd.choice(['-','']),i,k) for i in list]        
    else:
        draft = ['{}{}{}'.format(rnd.choice(['-',''])if list.index(i)<1 else rnd.choice(['-','+']),i, '*x^'+str(k-list.index(i)) \
        if list.index(i)<len(list)-1 else rnd.choice(['*x',''])) for i in list]
    result= ''.join(map(str,draft)).replace('^1','')+'=0'

    return result

with open('mult.txt','w') as f:
    f.write(Polynom(k))