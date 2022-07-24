# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from itertools import count
import random as rnd

n = 5

def PolyGen(n):
    draft =[rnd.randint(0,6) for i in range(n+1)]
    fill_in=[]
    for i in range(len(draft)):
        sign=rnd.choice(['-','+'])
        if draft[i]==0:
            continue
        elif i<n-1:
            mult=''.join('^{}'.format(n-i))
            temp='x'
        elif i==n-1:
            mult=''
            temp='x'
        else:
            temp=''
            mult=''
        fill_in.append('{}{}{}{}'.format(sign,draft[i],temp,mult))
    result=''.join(map(str,fill_in))+'=0'
    if result[0]=='+':
        return result[1:]
    return result

def Ext(string):
    poly=string.replace('+','')
    l1=[]
    point=0
    start = 0
    ind=0
    for i in range(poly.count('x')):
        item='x'
        ind=poly.index(item, start)
        if poly[ind+1]=='^':
            l1.append((poly[point:ind],poly[ind+2]))
            start=ind+3
            point=ind+3
        else :
            l1.append((poly[point:ind],'1'))
            
    if poly[ind+1] =='^':
        l1.append((poly[ind+2:-2],'0'))
    elif poly[ind+1] =='=':
        pass
    else:
        l1.append((poly[ind+1:-2],'0'))
        
    

    return l1

# Генерируем два многочлена с разными степенями k и l
k,l=5,4
poly1=PolyGen(k) #'-2x^5+2x^4+1x^3+3x^2=0' #
# poly2=PolyGen(l)

# print(poly2)
# print(Ext(poly2))

# Формируем строки для записи в файл и записываем коэфициенты в файлы poly1 и poly2
polystr=Ext(poly1)
print(poly1)
print(polystr)

exit()
sl=l+1
if k>l:
    sl=k+1
p1result=['0']*sl

for i in range(len(p1result)-1,-1,-1):
    for j in range(len(polystr)):
        if int(polystr[j][1])==i:
            p1result[len(p1result)-1-i]= polystr[j][0]

with open ('poly1.txt', 'w') as p1:
    p1.writelines("%s " % i for i in p1result)

exit()
with open ('poly2.txt', 'w') as p2:
    p2.writelines('%s ' % rnd.randint(-20,20) for i in range(4))

# Суммируем многочлены
with open ('poly1.txt', 'r') as p1: 
    r1 =p1.read().split()

with open ('poly2.txt', 'r') as p2: 
    r2 =p2.read().split()

with open ('polyresult.txt' , 'w') as pr:
    pr.writelines('%s ' % i for i in map(lambda x,y: x+y, map(int,r1),map(int,r2)))