# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 в виде  x^2 + 5*x - 3

import random as rnd

k = 5

def PolyGen(k):
    draft =[rnd.randint(0,100) for i in range(k+1)]
    fill_in=[]
    sign=rnd.choice(['-','+'])
    mult=''
    temp='x'
    for i in range(len(draft)):
        if draft[i]==0:
            continue
        elif i<k-1:
            mult='^{}'.format(k-i)
        elif i==k-1:
            mult=''
        else:
            temp=''
        fill_in.append('{}{}{}{}'.format(sign,draft[i],temp,mult))
    result=''.join(map(str,fill_in))+'=0'
    if result[0]=='+':
        return result[1:]
    return result

with open('mult.txt','w') as f:
    f.write(PolyGen(k))

# Проба пера
# def Polynom (k):
#     list =[rnd.randint(0,100) for i in range(rnd.randint(1,4))]
#     if len(list)==1:
#         draft = ['{}{}*x^{}'.format(rnd.choice(['-','']),i,k) for i in list]        
#     else:
#         draft = ['{}{}{}'.format(rnd.choice(['-',''])if list.index(i)<1 else rnd.choice(['-','+']),i, '*x^'+str(k-list.index(i)) \
#         if list.index(i)<len(list)-1 else rnd.choice(['*x',''])) for i in list]
#     fill_in= ''.join(map(str,draft)).replace('^1','')+'=0'

#     return fill_in

# with open('mult.txt','w') as f:
#     f.write(Polynom(k))