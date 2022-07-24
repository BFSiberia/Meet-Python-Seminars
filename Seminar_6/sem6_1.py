# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    # *Пример:* 
    # 2+2 => 4; 
    # 1+2*3 => 7; 
    # 1-2*3 => -5;
    # - Добавьте возможность использования скобок, меняющих приоритет операций.    
    # *Пример:*    
    # 1+2*3 => 7;   
    # (1+2)*3 => 9;

def Breckets(x):
    def Calc(x):
        result=0
        while "*" in x:
            ind = x.index('*')
            result=x[ind-1]*x[ind+1]
            x[ind-1]=result
            del x[ind:ind+2]

        while "/" in x:
            ind = x.index('/')
            result=x[ind-1]/x[ind+1]
            x[ind-1]=int(result)
            del x[ind:ind+2]

        while "-" in x:
            ind = x.index('-')
            result=x[ind-1]-x[ind+1]
            x[ind-1]=result
            del x[ind:ind+2]

        while '+' in x:
            ind = x.index('+')
            result=x[ind-1]+x[ind+1]
            x[ind-1]=result
            del x[ind:ind+2]
        return x[0]

    while '(' in x:
        brecketO = x.index('(')
        brecketC=x.index(')')
        x[brecketO]=Calc(x[brecketO+1:brecketC])
        del x[brecketO+1:brecketC+1]
    return Calc(x)

s1 = '5*(3-6)/(2+1)'
list='+,-,*,/,),('
x=[]

for i in s1:
    if i not in list:
        x.append(int(i))
    else:
        x.append(i)

print(Breckets(x))
print(eval(s1))